import engine


def draw_board_uni_gen(piece: str, color: str, sep_before: bool):
	# offsets from the base king
	piece_adds = {
		'k': 0,
		'q': 1,
		'r': 2,
		'b': 3,
		'n': 4,
		'p': 5
	}
	add = piece_adds.get(piece, 0)
	if color == 'b':
		add += 6  # black king is 6 behind white king
	if piece == '':
		uni_piece = ' '  # blank square
	else:
		uni_piece = chr(0x2654 + add)  # 0x2654: white king + add: offsets
	if sep_before:  # add seperator before piece (only if it's not the first column)
		print('|', end = '')
	print(f'  {uni_piece}  ', end = '')


def draw_board(pieces: dict):
	board = engine.pieces_to_board(pieces)  # generate board
	print('\n' * 16)  # clear previous board
	print('    a     b     c     d     e     f     g     h')
	for line_n, line in enumerate(board):
		line_n = 8 - line_n  # convert pythonic numbers to chess numbers
		if line_n != 0:  # add separators before every line except the first
			print('  -----|-----|-----|-----|-----|-----|-----|-----')
		print(f'{line_n} ', end = '')
		for i, col in enumerate(line):
			draw_board_uni_gen(col[0] if col else '', col[1] if col else '', i != 0)  # generate unicode representation of chess piece (and output it)
		print(f' {line_n}')
	print('    a     b     c     d     e     f     g     h')
