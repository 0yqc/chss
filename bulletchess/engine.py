import bulletchess as bc
from bulletchess import utils as bcutils

maps = {
	'mapped': [bc.PAWN, bc.KNIGHT],
	bc.WHITE: {
		bc.PAWN: {
			bc.A8: 0.000, bc.B8: 0.000, bc.C8: 0.000, bc.D8: 0.000, bc.E8: 0.000, bc.F8: 0.000, bc.G8: 0.000, bc.H8: 0.000,
			bc.A7: 4.250, bc.B7: 4.500, bc.C7: 4.625, bc.D7: 4.750, bc.E7: 4.750, bc.F7: 4.625, bc.G7: 4.500, bc.H7: 4.250,
			bc.A6: 2.000, bc.B6: 2.500, bc.C6: 2.750, bc.D6: 3.000, bc.E6: 3.000, bc.F6: 2.750, bc.G6: 2.250, bc.H6: 2.000,
			bc.A5: 1.750, bc.B5: 2.250, bc.C5: 2.500, bc.D5: 2.750, bc.E5: 2.750, bc.F5: 2.500, bc.G5: 2.250, bc.H5: 1.750,
			bc.A4: 1.500, bc.B4: 2.000, bc.C4: 2.250, bc.D4: 2.500, bc.E4: 2.500, bc.F4: 2.250, bc.G4: 2.000, bc.H4: 1.500,
			bc.A3: 1.250, bc.B3: 1.500, bc.C3: 1.625, bc.D3: 1.750, bc.E3: 1.750, bc.F3: 1.625, bc.G3: 1.500, bc.H3: 1.250,
			bc.A2: 1.000, bc.B2: 1.000, bc.C2: 1.000, bc.D2: 1.000, bc.E2: 1.000, bc.F2: 1.000, bc.G2: 1.000, bc.H2: 1.000,
			bc.A1: 0.000, bc.B1: 0.000, bc.C1: 0.000, bc.D1: 0.000, bc.E1: 0.000, bc.F1: 0.000, bc.G1: 0.000, bc.H1: 0.000,
		},
		bc.KNIGHT: {
			bc.A8: 0.750 + 0.825, bc.B8: 1.000 + 0.825, bc.C8: 0.750 + 0.825, bc.D8: 1.000 + 0.825, bc.E8: 1.000 + 0.825, bc.F8: 0.750 + 0.825, bc.G8: 1.000 + 0.825, bc.H8: 0.750 + 0.825,
			bc.A7: 1.000 + 0.750, bc.B7: 0.750 + 0.750, bc.C7: 1.500 + 0.750, bc.D7: 1.500 + 0.750, bc.E7: 1.500 + 0.750, bc.F7: 1.500 + 0.750, bc.G7: 0.750 + 0.750, bc.H7: 1.000 + 0.750,
			bc.A6: 0.750 + 0.625, bc.B6: 1.500 + 0.625, bc.C6: 1.750 + 0.625, bc.D6: 1.625 + 0.625, bc.E6: 1.625 + 0.625, bc.F6: 1.750 + 0.625, bc.G6: 1.500 + 0.625, bc.H6: 0.750 + 0.625,
			bc.A5: 1.000 + 0.500, bc.B5: 1.500 + 0.500, bc.C5: 1.625 + 0.500, bc.D5: 2.000 + 0.500, bc.E5: 2.000 + 0.500, bc.F5: 1.625 + 0.500, bc.G5: 1.500 + 0.500, bc.H5: 1.000 + 0.500,
			bc.A4: 1.000 + 0.325, bc.B4: 1.500 + 0.325, bc.C4: 1.625 + 0.325, bc.D4: 2.000 + 0.325, bc.E4: 2.000 + 0.325, bc.F4: 1.625 + 0.325, bc.G4: 1.500 + 0.325, bc.H4: 1.000 + 0.325,
			bc.A3: 0.750 + 0.250, bc.B3: 1.500 + 0.250, bc.C3: 1.750 + 0.250, bc.D3: 1.625 + 0.250, bc.E3: 1.625 + 0.250, bc.F3: 1.750 + 0.250, bc.G3: 1.500 + 0.250, bc.H3: 0.750 + 0.250,
			bc.A2: 1.000 + 0.125, bc.B2: 0.750 + 0.125, bc.C2: 1.500 + 0.125, bc.D2: 1.500 + 0.125, bc.E2: 1.500 + 0.125, bc.F2: 1.500 + 0.125, bc.G2: 0.750 + 0.125, bc.H2: 1.000 + 0.125,
			bc.A1: 1.000 + 0.000, bc.B1: 1.000 + 0.000, bc.C1: 0.750 + 0.000, bc.D1: 1.000 + 0.000, bc.E1: 1.000 + 0.000, bc.F1: 0.750 + 0.000, bc.G1: 1.000 + 0.000, bc.H1: 0.750 + 0.000,
		},
		'other': {
			bc.A8: 1.500, bc.B8: 1.750, bc.C8: 2.000, bc.D8: 2.250, bc.E8: 2.250, bc.F8: 2.000, bc.G7: 1.750, bc.H8: 1.500,
			bc.A7: 1.500, bc.B7: 1.750, bc.C7: 2.000, bc.D7: 2.250, bc.E7: 2.250, bc.F7: 2.000, bc.G8: 1.750, bc.H7: 1.500,
			bc.A6: 1.500, bc.B6: 1.750, bc.C6: 2.000, bc.D6: 2.250, bc.E6: 2.250, bc.F6: 2.000, bc.G6: 1.750, bc.H6: 1.500,
			bc.A5: 1.500, bc.B5: 1.625, bc.C5: 1.825, bc.D5: 2.125, bc.E5: 2.125, bc.F5: 1.875, bc.G5: 1.625, bc.H5: 1.500,
			bc.A4: 1.125, bc.B4: 1.500, bc.C4: 1.750, bc.D4: 2.000, bc.E4: 2.000, bc.F4: 1.750, bc.G4: 1.500, bc.H4: 1.125,
			bc.A3: 1.000, bc.B3: 1.250, bc.C3: 1.500, bc.D3: 1.625, bc.E3: 1.625, bc.F3: 1.500, bc.G3: 1.250, bc.H3: 1.000,
			bc.A2: 0.750, bc.B2: 0.825, bc.C2: 1.000, bc.D2: 1.125, bc.E2: 1.125, bc.F2: 1.000, bc.G2: 0.825, bc.H2: 0.750,
			bc.A1: 0.500, bc.B1: 0.625, bc.C1: 0.750, bc.D1: 0.875, bc.E1: 0.875, bc.F1: 0.750, bc.G1: 0.625, bc.H1: 0.500,
		}
	},
	bc.BLACK: {}  # will be autofilled
}

# convert white value maps to black value maps
for map in maps[bc.WHITE]:
	maps[bc.BLACK].update({map: {}})
	for square in maps[bc.WHITE][map]:
		maps[bc.BLACK][map].update({bc.SQUARES_FLIPPED[square.index()]: maps[bc.WHITE][map][square]}) # bc.SQUARES_FLIPPED[square.index()] essentially flips/mirrors the square


def evaluate(board: bc.Board) -> float:
	# game over
	if board in bc.CHECKMATE:
		return float('inf') if board.turn == bc.BLACK else float('-inf')
	if board in bc.DRAW:
		return 0
	
	score = 0

	pawn_const = 0.1875 * len(board.__getitem__(bc.PAWN)) # 3 / 16; 0 to 3
	piece_values = {
		bc.KING: 0,
		bc.PAWN: 1,
		bc.KNIGHT: 1.5 + pawn_const,
		bc.BISHOP: 4.5 - pawn_const,
		bc.ROOK: 6.5 - pawn_const,
		bc.QUEEN: 10.5 - pawn_const
	}

	# piece loop
	for piece_type in bc.PIECE_TYPES:
		for piece in board.__getitem__((bc.WHITE, piece_type)):
			# piece values
			if piece_type in maps['mapped']:
				score += piece_values[piece_type] * maps[bc.WHITE][piece_type][piece]
			else:
				score += piece_values[piece_type] * maps[bc.WHITE]['other'][piece]
		for piece in board.__getitem__((bc.BLACK, piece_type)):
			# piece values
			if piece_type in maps['mapped']:
				score -= piece_values[piece_type] * maps[bc.BLACK][piece_type][piece]
			else:
				score -= piece_values[piece_type] * maps[bc.BLACK]['other'][piece]

	# check check
	if board in bc.CHECK:
		score += 10 if board.turn == bc.BLACK else -10
		
	# attacked squares / enemy pieces // protection
	for square in bcutils.attack_mask(board, bc.WHITE):
		score += 0.25 * maps[bc.WHITE]['other'][square]  # 10 / 40
		score += 1 if square in bcutils.white_bitboard(board) else 0
		score += 1 if square in bcutils.black_bitboard(board) else 0
	for square in bcutils.attack_mask(board, bc.BLACK):
		score -= 0.25 * maps[bc.BLACK]['other'][square]  # 10 / 40
		score -= 1 if square in bcutils.white_bitboard(board) else 0
		score -= 1 if square in bcutils.black_bitboard(board) else 0

	# mobility
	score += 0.0625 * bcutils.mobility(board) # 1 / 16
	
	return score


def gen(board: bc.Board, depth: int = 4, alpha: float = float('-inf'), beta: float = float('-inf'), return_move: bool = False) -> float | bc.Move | None:
	legal_moves = board.legal_moves()
	if depth == 0 or not legal_moves:
		return None if return_move else evaluate(board)
	if board.turn == bc.WHITE:  # maximizing
		score = float('-inf')
		for move in legal_moves:
			board.apply(move)
			gend = gen(board, depth - 1, alpha = alpha, beta = beta)
			board.undo()
			if gend > score:
				score = gend
				bmove = move
			if score >= beta:
				break
			alpha = max(alpha, score)
	else:  # minimizing
		score = float('inf')
		for move in legal_moves:
			board.apply(move)
			gend = gen(board, depth - 1, alpha = alpha, beta = beta)
			board.undo()
			if gend < score:
				score = gend
				bmove = move
			if score <= alpha:
				break
			beta = min(beta, score)
	return bmove if return_move else score
