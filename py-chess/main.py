import chess, chess.svg, chess.engine
import engine as chss_engine


def draw_board(board):
	if board.is_check():
		fill = {list(board.pieces(chess.KING, board.turn))[0]: '#7f0000'}
	else:
		fill = {}
	if len(board.move_stack):
		svg = chess.svg.board(board, lastmove = board.move_stack[-1], fill = fill)
	else:
		svg = chess.svg.board(board)
	file = open('/tmp/board.svg', 'w')
	file.write(svg)
	file.close()


def fix_board(board):
	color = None
	while True:
		inp = input('SAN / pop / color / exit: ').strip()
		if inp == 'exit':
			return board, color
		elif inp == 'pop':
			board.pop()
		elif inp == 'black':
			color = chess.BLACK
		elif inp == 'white':
			color = chess.WHITE
		else:
			board.turn = chess.WHITE if input('Color: ').lower() == 'white' else chess.BLACK
			board.push_san(inp)
		draw_board(board)


def main():
	board = chess.Board()

	file = open('/tmp/board.svg', 'w')
	file.write(chess.svg.board(board))
	file.close()

	player = {
		chess.WHITE: 'chss',
		chess.BLACK: 'chss'
	}
	
	if 'stockfish' in player.values():
		stockfish_t = 1
		engine = chess.engine.SimpleEngine.popen_uci('/home/luna/docs/stockfish/stockfish-ubuntu-x86-64-avx2')
	
	while not board.is_game_over():
		if player[board.turn] == 'user':
				legal_move = False
				while not legal_move:
					legal_move = True
					inp = input('Your move (algebraic notation): ').strip()
					if inp == 'fix':
						board, color = fix_board(board)
						board.turn = color
					elif inp == 'pop':
						board.pop()
						board.pop()
					else:
						try:
							move = board.parse_san(inp)
							san = board.san(move)
							board.push(move)
							score = chss_engine.evaluate(board)
							print(f'Move: {san}; Score: {score}')
							draw_board(board)
						except chess.IllegalMoveError:
							print('Illegal Move. Try again.')
							legal_move = False
						except chess.InvalidMoveError:
							print('Bad Notation. Try again.')
							legal_move = False
						except chess.AmbiguousMoveError:
							print('Ambiguous Move. Try again.')
							legal_move = False
						except Exception as e:
							print(f'Unknown Error. Check notation and try again. Error: {e}')
		elif player[board.turn] == 'stockfish':
			move = engine.play(board, chess.engine.Limit(time = stockfish_t)).move
			san = board.san(move)
			board.push(move)
			score = chss_engine.evaluate(board)
			print(f'Move: {san}; Score: {score}')
			draw_board(board)
		elif player[board.turn] == 'chss':
			move = chss_engine.generate_init(board, 5, board.turn)
			if move is not None:
				san = board.san(move)
				board.push(move)
				score = chss_engine.evaluate(board)
				print(f'Move: {san}; Score: {score}')
				draw_board(board)
			else:
				break

if __name__ == '__main__':
	main()