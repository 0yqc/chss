# legal moves
moves = {
	'k': [
		[-1, -1], [-1, 0], [-1, 1],
		[0, -1], [0, 1],
		[1, -1], [1, 0], [1, 1]
	],
	'q': [
		[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
		[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],
		[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],
		[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],
		[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
		[1, -1], [2, -1], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],
		[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
		[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]
	],
	'r': [
		[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],
		[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0],
		[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7],
		[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]
	],
	'b': [
		[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7],
		[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7],
		[1, -1], [2, -1], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7],
		[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]
	],
	'n': [
		[-1, -2], [-2, -1], [-2, 1], [-1, 2],
		[1, -2], [2, -1], [2, 1], [1, 2]
	],
	'p': [
		[1, 0], [2, 0],
		[1, 1], [1, -1]
	]
}


def pieces_to_board(pieces: dict):
	# init
	board = [
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
		[[], [], [], [], [], [], [], []],
	]
	for color in pieces:
		for piece in pieces[color]:
			for individual in pieces[color][piece]:
				board[individual[0]][individual[1]] = [piece, color]  # set content of the field
	return board


def chesscol_to_pycol(col: str):
	conversion = {
		'a': 0,
		'b': 1,
		'c': 2,
		'd': 3,
		'e': 4,
		'f': 5,
		'g': 6,
		'h': 7
	}
	return conversion.get(col)


def get_moves(piece: str, coordinates: list, board: list):
	print(moves)

def algebraic_to_pieces(algebraic: str, pieces: dict, color: str, castling: bool):
	board = pieces_to_board(pieces)
	capture, check, mate, moved = False, False, False, False
	promotion, dep_col, dep_line = None, None, None

	if algebraic == '0-0' or algebraic == '0-0-0':
		line = 0 if color == 'b' else 7
		if algebraic == '0-0' and not (board[line][5] or board[line][6]) and castling:
			pieces[color]['k'][0] = [line, 6]
			pieces[color]['r'][1] = [line, 5]
			castling = False
			moved = True
		elif algebraic == '0-0-0' and not (board[line][1] or board[line][2] or board[line][3]) and castling:
			pieces[color]['k'][0] = [line, 2]
			pieces[color]['r'][0] = [line, 3]
			castling = False
			moved = True
	else:
		algebraic = [char for char in algebraic]
		if 'x' in algebraic:
			capture = True
			algebraic.remove('x')
		if '+' in algebraic:
			check = True
			algebraic.remove('+')
		if '#' in algebraic:
			mate = True
			algebraic.remove('#')
		if algebraic[0].isupper():
			piece = algebraic[0].lower()
			algebraic.pop(0)
		else:
			piece = 'p'
		if algebraic[-1].isupper():
			promotion = algebraic[-1].lower()
			algebraic.pop(-1)
		try:
			line = 8 - int(algebraic[-1])  # convert chess notation to pythonic
			col = chesscol_to_pycol(algebraic[-2])
		except ValueError:
			return pieces, castling, False
		if len(algebraic) == 2:
			dep_line = 8 - int(algebraic[1])
			dep_col = chesscol_to_pycol(algebraic[0])
		elif algebraic[0].isdigit():
			dep_line = 8 - int(algebraic[0])
		else:
			dep_col = chesscol_to_pycol(algebraic[0])

		for individual in pieces[color][piece]:
			moves = get_moves(piece, individual, board)

	return pieces, castling, moved

# identify correct piece if multiple applicable (implement rules), good commenting, code rework?
