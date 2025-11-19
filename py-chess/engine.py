import chess
import time

attack_values = {
	chess.WHITE: {
		chess.A8: .5, chess.B8: .5, chess.C8: .5, chess.D8: .5, chess.E8: .5, chess.F8: .5, chess.G8: .5, chess.H8: .5,
		chess.A7: .5, chess.B7: .75, chess.C7: .75, chess.D7: .75, chess.E7: .75, chess.F7: .75, chess.G7: .75, chess.H7: .5,
		chess.A6: .5, chess.B6: 1, chess.C6: 1, chess.D6: 1, chess.E6: 1, chess.F6: 1, chess.G6: .1, chess.H6: .5,
		chess.A5: .5, chess.B5: 1, chess.C5: 1, chess.D5: 1.5, chess.E5: 1.5, chess.F5: 1, chess.G5: 1, chess.H5: .5,
		chess.A4: .5, chess.B4: 1, chess.C4: 1, chess.D4: 1.5, chess.E4: 1.5, chess.F4: 1, chess.G4: 1, chess.H4: .5,
		chess.A3: .5, chess.B3: 1, chess.C3: 1, chess.D3: 1, chess.E3: 1, chess.F3: 1, chess.G3: 1, chess.H3: .5,
		chess.A2: .5, chess.B2: .75, chess.C2: .75, chess.D2: .75, chess.E2: .75, chess.F2: .75, chess.G2: .75, chess.H2: .5,
		chess.A1: .5, chess.B1: .5, chess.C1: .5, chess.D1: .5, chess.E1: .5, chess.F1: .5, chess.G1: .5, chess.H1: .5
	},
	chess.BLACK: {
		chess.A8: .5, chess.B8: .5, chess.C8: .5, chess.D8: .5, chess.E8: .5, chess.F8: .5, chess.G8: .5, chess.H8: .5,
		chess.A7: .5, chess.B7: .75, chess.C7: .75, chess.D7: .75, chess.E7: .75, chess.F7: .75, chess.G7: .75, chess.H7: .5,
		chess.A6: .5, chess.B6: 1, chess.C6: 1, chess.D6: 1, chess.E6: 1, chess.F6: 1, chess.G6: .1, chess.H6: .5,
		chess.A5: .5, chess.B5: 1, chess.C5: 1, chess.D5: 1.5, chess.E5: 1.5, chess.F5: 1, chess.G5: 1, chess.H5: .5,
		chess.A4: .5, chess.B4: 1, chess.C4: 1, chess.D4: 1.5, chess.E4: 1.5, chess.F4: 1, chess.G4: 1, chess.H4: .5,
		chess.A3: .5, chess.B3: 1, chess.C3: 1, chess.D3: 1, chess.E3: 1, chess.F3: 1, chess.G3: 1, chess.H3: .5,
		chess.A2: .5, chess.B2: .75, chess.C2: .75, chess.D2: .75, chess.E2: .75, chess.F2: .75, chess.G2: .75, chess.H2: .5,
		chess.A1: .5, chess.B1: .5, chess.C1: .5, chess.D1: .5, chess.E1: .5, chess.F1: .5, chess.G1: .5, chess.H1: .5
	}
}
value_maps = {
	chess.WHITE: {
		chess.PAWN: {
			chess.A8: 0, chess.B8: 0, chess.C8: 0, chess.D8: 0, chess.E8: 0, chess.F8: 0, chess.G8: 0, chess.H8: 0,
			chess.A7: 2, chess.B7: 2, chess.C7: 2.5, chess.D7: 2.5, chess.E7: 2.5, chess.F7: 2.5, chess.G7: 2, chess.H7: 2,
			chess.A6: 1.5, chess.B6: 2, chess.C6: 2, chess.D6: 2.5, chess.E6: 2.5, chess.F6: 2, chess.G6: 2, chess.H6: 1.5,
			chess.A5: 1, chess.B5: 1, chess.C5: 1.5, chess.D5: 2, chess.E5: 2, chess.F5: 1.5, chess.G5: 1, chess.H5: 1,
			chess.A4: .75, chess.B4: .75, chess.C4: 1, chess.D4: 1.5, chess.E4: 1.5, chess.F4: 1, chess.G4: .75, chess.H4: .75,
			chess.A3: .625, chess.B3: .75, chess.C3: .75, chess.D3: .75, chess.E3: .75, chess.F3: .75, chess.G3: .75, chess.H3: .625,
			chess.A2: .5, chess.B2: .5, chess.C2: .5, chess.D2: .5, chess.E2: .5, chess.F2: .5, chess.G2: .5, chess.H2: .5,
			chess.A1: 0, chess.B1: 0, chess.C1: 0, chess.D1: 0, chess.E1: 0, chess.F1: 0, chess.G1: 0, chess.H1: 0
		},
		'other': {
			chess.A8: .5, chess.B8: .5, chess.C8: .5, chess.D8: .5, chess.E8: .5, chess.F8: .5, chess.G8: .5, chess.H8: .5,
			chess.A7: .5, chess.B7: .75, chess.C7: .75, chess.D7: .75, chess.E7: .75, chess.F7: .75, chess.G7: .75, chess.H7: .5,
			chess.A6: .5, chess.B6: 1, chess.C6: 1, chess.D6: 1, chess.E6: 1, chess.F6: 1, chess.G6: .1, chess.H6: .5,
			chess.A5: .5, chess.B5: 1, chess.C5: 1, chess.D5: 1.5, chess.E5: 1.5, chess.F5: 1, chess.G5: 1, chess.H5: .5,
			chess.A4: .5, chess.B4: 1, chess.C4: 1, chess.D4: 1.5, chess.E4: 1.5, chess.F4: 1, chess.G4: 1, chess.H4: .5,
			chess.A3: .5, chess.B3: 1, chess.C3: 1, chess.D3: 1, chess.E3: 1, chess.F3: 1, chess.G3: 1, chess.H3: .5,
			chess.A2: .5, chess.B2: .75, chess.C2: .75, chess.D2: .75, chess.E2: .75, chess.F2: .75, chess.G2: .75, chess.H2: .5,
			chess.A1: .5, chess.B1: .5, chess.C1: .5, chess.D1: .5, chess.E1: .5, chess.F1: .5, chess.G1: .5, chess.H1: .5
		}
	},
	chess.BLACK: {
		chess.PAWN: {
			chess.A8: 0, chess.B8: 0, chess.C8: 0, chess.D8: 0, chess.E8: 0, chess.F8: 0, chess.G8: 0, chess.H8: 0,
			chess.A7: .5, chess.B7: .5, chess.C7: .5, chess.D7: .5, chess.E7: .5, chess.F7: .5, chess.G7: .5, chess.H7: .5,
			chess.A6: .625, chess.B6: .75, chess.C6: .75, chess.D6: .75, chess.E6: .75, chess.F6: .75, chess.G6: .75, chess.H6: .625,
			chess.A5: .75, chess.B5: .75, chess.C5: 1, chess.D5: 1.5, chess.E5: 1.5, chess.F5: 1, chess.G5: .75, chess.H5: .75,
			chess.A4: 1, chess.B4: 1, chess.C4: 1.5, chess.D4: 2, chess.E4: 2, chess.F4: 1.5, chess.G4: 1, chess.H4: 1,
			chess.A3: 1.5, chess.B3: 2, chess.C3: 2, chess.D3: 2.5, chess.E3: 2.5, chess.F3: 2, chess.G3: 2, chess.H3: 1.5,
			chess.A2: 2, chess.B2: 2, chess.C2: 2.5, chess.D2: 2.5, chess.E2: 2.5, chess.F2: 2.5, chess.G2: 2, chess.H2: 2,
			chess.A1: 0, chess.B1: 0, chess.C1: 0, chess.D1: 0, chess.E1: 0, chess.F1: 0, chess.G1: 0, chess.H1: 0
		},
		'other': {
			chess.A8: .5, chess.B8: .5, chess.C8: .5, chess.D8: .5, chess.E8: .5, chess.F8: .5, chess.G8: .5, chess.H8: .5,
			chess.A7: .5, chess.B7: .75, chess.C7: .75, chess.D7: .75, chess.E7: .75, chess.F7: .75, chess.G7: .75, chess.H7: .5,
			chess.A6: .5, chess.B6: 1, chess.C6: 1, chess.D6: 1, chess.E6: 1, chess.F6: 1, chess.G6: .1, chess.H6: .5,
			chess.A5: .5, chess.B5: 1, chess.C5: 1, chess.D5: 1.5, chess.E5: 1.5, chess.F5: 1, chess.G5: 1, chess.H5: .5,
			chess.A4: .5, chess.B4: 1, chess.C4: 1, chess.D4: 1.5, chess.E4: 1.5, chess.F4: 1, chess.G4: 1, chess.H4: .5,
			chess.A3: .5, chess.B3: 1, chess.C3: 1, chess.D3: 1, chess.E3: 1, chess.F3: 1, chess.G3: 1, chess.H3: .5,
			chess.A2: .5, chess.B2: .75, chess.C2: .75, chess.D2: .75, chess.E2: .75, chess.F2: .75, chess.G2: .75, chess.H2: .5,
			chess.A1: .5, chess.B1: .5, chess.C1: .5, chess.D1: .5, chess.E1: .5, chess.F1: .5, chess.G1: .5, chess.H1: .5
		}
	}
}


def evaluate_old(board: chess.Board):
	if board.is_checkmate() and board.turn == chess.BLACK:  # after checkmate it would be the other persons turn
		return float('inf')  # checkmate for white
	elif board.is_checkmate():
		return float('-inf')  # checkmate for black

	white_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
	black_pawns = len(board.pieces(chess.PAWN, chess.BLACK))

	piece_values = {
		chess.WHITE: {
			chess.KING: 0,
			chess.PAWN: 1,
			chess.KNIGHT: 1.5 + (3 / 16 * (white_pawns + black_pawns)),
			chess.BISHOP: 3,
			chess.ROOK: 8 - (4 / 16 * (black_pawns + black_pawns)),
			chess.QUEEN: 9
		},
		chess.BLACK: {
			chess.KING: 0,
			chess.PAWN: 1,
			chess.KNIGHT: 1.5 + (3 / 16 * (black_pawns + black_pawns)),
			chess.BISHOP: 3,
			chess.ROOK: 8 - (4 / 16 * (black_pawns + black_pawns)),
			chess.QUEEN: 9
		}
	}
	score = 0

	for piece_type in chess.PIECE_TYPES:
		# white
		for square in board.pieces(piece_type, chess.WHITE):
			# material difference and position
			if piece_type in value_maps:
				score += 3 * piece_values[chess.WHITE][piece_type] * value_maps[chess.WHITE][piece_type][square]
			else:
				score += 3 * piece_values[chess.WHITE][piece_type] * value_maps[chess.WHITE]['other'][square]
			# attacked
			score += .25 * piece_values[chess.WHITE][piece_type] * attack_values[chess.WHITE][square] if board.attackers(chess.WHITE, square) else 0
			score -= .25 * piece_values[chess.WHITE][piece_type] * attack_values[chess.WHITE][square] if board.attackers(chess.BLACK, square) else 0
			score += 1 / 16 * piece_values[chess.WHITE][piece_type] * len(board.attackers(chess.WHITE, square)) * attack_values[chess.WHITE][square]
			score -= 1 / 16 * piece_values[chess.WHITE][piece_type] * len(board.attackers(chess.BLACK, square)) * attack_values[chess.WHITE][square]
			# pawn protection
			if piece_type == chess.PAWN:
				for attacker in board.attackers(chess.WHITE, square):
					if attacker == chess.PAWN:
						score -= 1
		# black
		for square in board.pieces(piece_type, chess.BLACK):
			# material difference and position
			if piece_type in value_maps:
				score -= 3 * piece_values[chess.BLACK][piece_type] * value_maps[chess.BLACK][piece_type][square]
			else:
				score -= 3 * piece_values[chess.BLACK][piece_type] * value_maps[chess.BLACK]['other'][square]
			# attacked
			score += .25 * piece_values[chess.BLACK][piece_type] * attack_values[chess.BLACK][square] if board.attackers(chess.WHITE, square) else 0
			score -= .25 * piece_values[chess.BLACK][piece_type] * attack_values[chess.BLACK][square] if board.attackers(chess.BLACK, square) else 0
			score += 1 / 16 * piece_values[chess.BLACK][piece_type] * len(board.attackers(chess.WHITE, square)) * attack_values[chess.BLACK][square]
			score -= 1 / 16 * piece_values[chess.BLACK][piece_type] * len(board.attackers(chess.BLACK, square)) * attack_values[chess.BLACK][square]
			# pawn protection
			if piece_type == chess.PAWN:
				for attacker in board.attackers(chess.BLACK, square):
					if attacker == chess.PAWN:
						score -= 1

	# pawns 'replace' missing bishop (pawns on the same color as missing bishop is good)
	if len(board.pieces(chess.BISHOP, chess.WHITE)) == 1:
		if list(board.pieces(chess.BISHOP, chess.WHITE))[0] % 2:  # bishop on white filed
			for pawn in board.pieces(chess.PAWN, chess.WHITE):
				if pawn % 2:  # pawn on white field
					score += 2
				else:
					score -= 2
		else:  # bishop on black field
			for pawn in board.pieces(chess.PAWN, chess.WHITE):
				if pawn % 2:  # pawn on white field
					score -= 2
				else:
					score += 2
	if len(board.pieces(chess.BISHOP, chess.BLACK)) == 1:
		if list(board.pieces(chess.BISHOP, chess.BLACK))[0] % 2:  # bishop on white filed
			for pawn in board.pieces(chess.PAWN, chess.BLACK):
				if pawn % 2:  # pawn on white field
					score += 2
				else:
					score -= 2
		else:  # bishop on black field
			for pawn in board.pieces(chess.PAWN, chess.BLACK):
				if pawn % 2:  # pawn on white field
					score -= 2
				else:
					score += 2

	# check check
	turn = board.turn
	board.turn = chess.WHITE
	score -= 5 if board.is_check() else 0
	board.turn = chess.BLACK
	score += 5 if board.is_check() else 0
	board.turn = turn

	return score


def evaluate(board: chess.Board):
	if board.is_checkmate():
		return float('inf') if board.turn == chess.BLACK else float('-inf')
	board_str = str(board)
	material = {
		'white': {
			'pawn': board_str.count('P'),
			'knight': board_str.count('N'),
			'bishop': board_str.count('B'),
			'rook': board_str.count('R'),
			'queen': board_str.count('Q'),
			'king': 1 if 'K' in board_str else 0
		},
		'black': {
			'pawn': board_str.count('p'),
			'knight': board_str.count('n'),
			'bishop': board_str.count('b'),
			'rook': board_str.count('r'),
			'queen': board_str.count('q'),
			'king': 1 if 'k' in board_str else 0
		}
	}
	score = 1 * material['white']['pawn'] + (2 + 2/16 * (material['white']['pawn'] + material['black']['pawn'])) * material['white']['knight'] + 3 * material['white']['bishop'] + (7 - 4/16 * (material['white']['pawn'] + material['black']['pawn'])) * material['white']['rook'] + 9 * material['white']['queen']
	score -= 1 * material['black']['pawn'] + (2 + 2 / 16 * (material['white']['pawn'] + material['black']['pawn'])) * material['black']['knight'] + 3 * material['black']['bishop'] + (7 - 4 / 16 * (material['white']['pawn'] + material['black']['pawn'])) * material['black']['rook'] + 9 * material['black']['queen']

	if board.is_check():
		score += 5 if board.turn == chess.BLACK else -5
	return score


def generate_init(board: chess.Board, depth: int, color: chess.Color):
	alpha = float('-inf')
	beta = float('inf')
	score = float('inf')
	evaluate_n = 0
	evaluate_t = 0
	best_move = None
	if board.is_game_over():
		return None
	for move in board.legal_moves:
		board.push(move)
		value_gend = generate(board, depth - 1, alpha, beta, not color)
		board.pop()
		if value_gend < score:
			best_move = move
			score = value_gend
		if score <= alpha:
			break
		beta = min(beta, score)
	return best_move


def generate(board: chess.Board, depth: int, alpha: float, beta: float, color: chess.Color):
	if depth == 0 or board.is_game_over():
		score = evaluate(board)
		return score
	if color == chess.WHITE:
		score = float('-inf')
		for move in board.legal_moves:
			board.push(move)
			score = max(generate(board, depth - 1, alpha, beta, chess.BLACK), score)
			board.pop()
			if score >= beta:
				break
			alpha = max(alpha, score)
		return score
	else:
		score = float('inf')
		for move in board.legal_moves:
			board.push(move)
			score = min(generate(board, depth - 1, alpha, beta, chess.BLACK), score)
			board.pop()
			if score <= alpha:
				break
			beta = min(beta, score)
		return score
