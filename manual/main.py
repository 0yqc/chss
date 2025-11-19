import gui
import engine

game = True  # game running state

# initial piece positions:
pieces = {
	'b': {
		'k': [
			[0, 4]
		],
		'q': [
			[0, 3]
		],
		'r': [
			[0, 0], [0, 7]
		],
		'b': [
			[0, 2], [0, 5]
		],
		'n': [
			[0, 1], [0, 6]
		],
		'p': [
			[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]
		]
	},
	'w': {
		'k': [
			[7, 4]
		],
		'q': [
			[7, 3]
		],
		'r': [
			[7, 0], [7, 7]
		],
		'b': [
			[7, 2], [7, 5]
		],
		'n': [
			[7, 1], [7, 6]
		],
		'p': [
			[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7]
		]
	}
}
# castling allowed initially (wil be set to False once moved)
castling = True

while game:
	gui.draw_board(pieces)
	moved = False
	while not moved:
		pieces, castling, moved = engine.algebraic_to_pieces(input('Your move (algebraic notation): ').strip(), pieces, 'w', castling) # repeat if illegal move
		if not moved:
			print('Illegal move / Bad notation. Try again')
