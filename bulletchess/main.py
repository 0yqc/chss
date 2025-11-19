# install via pip
# pip install bulletchess (--break-system-packages)
import bulletchess as bc
# install via pip
# pip install python-chess (--break-system-packages)
import chess as pc
from chess import engine, svg
# local file for chss engine
import engine as chss


def board_draw(board: bc.Board) -> None:
	board = pc.Board(board.fen())  # bc board to pc board
	if len(board.move_stack) != 0:
		move = board.move_stack[-1]
	else:
		move = None
	fill = {}
	if board.is_checkmate():
		fill.update({list(board.pieces(pc.KING, board.turn))[0]: '#400000'})
	elif board.is_check():
		fill.update({list(board.pieces(pc.KING, board.turn))[0]: '#800000'})
	svg = pc.svg.board(board, lastmove = move, fill = fill)
	with open('/tmp/board.svg', 'w') as f:
		f.write(svg)
		f.close()


def apply_move(board: bc.Board, scores: list[float], move: bc.Move | None = None, san: str | None = None) -> tuple[list[float], Exception | None]:
	if move:
		san = move.san(board)
	elif san:
		try:
			move = bc.Move.from_san(san, board)
		except Exception as e:
			return scores, e
	if not move:
		return scores, None
	try:
		board.apply(move)
	except Exception as e:
		return scores, e
	scores.append(chss.evaluate(board))
	print(f'Move: {san};{' ' * max(12 - len(san), 0)} Score: {' ' * max(8 - len(str(round(scores[-1], 2)).removesuffix('.0')), 0)}{(round(scores[-1], 2))}; Diff: {(' ' * max(4 - len(str(round(scores[-1] - scores[-2], 3)).removesuffix('.0')), 0) + str(round(scores[-1] - scores[-2], 3))) if len(scores) != 1 else ' n/a'}')
	return scores, None


def main() -> None:
	board = bc.Board()
	board_draw(board)
	running = True
	scores = []

	players = {
		bc.WHITE: 'user',
		bc.BLACK: 'chss'
	}
	if 'stockfish' in players.values():
		path = '/home/luna/docs/stockfish/stockfish-ubuntu-x86-64-avx2'
		stockfish = pc.engine.SimpleEngine.popen_uci(path)
		time = 1

	while True:
		if board in bc.CHECKMATE:
			break
		if players[board.turn] == 'user':
			while True:
				san = input('Yor move (SAN): ')
				if san.startswith('undo'):
					n = san.removeprefix('undo')
					n = int(n) if n else 2
					for i in range(n):
						board.undo()
					break
				scores, exception = apply_move(board, scores, san = san)
				if exception:
					print(f'Error, check notation. {exception}')
				else:
					break
		elif players[board.turn] == 'stockfish':
			move = stockfish.play(pc.Board(board.fen()), engine.Limit(time = time)).move
			scores, _ = apply_move(board, scores, move = bc.Move.from_uci(str(move)))
		elif players[board.turn] == 'chss':
			move = chss.gen(board, return_move = True, depth = 6)
			scores, _ = apply_move(board, scores, move = move)
		board_draw(board)
	print(f'Game ended.')


if __name__ == '__main__':
	main()
