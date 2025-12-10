package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.Square.*
import com.github.bhlangonijr.chesslib.move.*
import kotlin.Double.Companion.NEGATIVE_INFINITY
import kotlin.Double.Companion.POSITIVE_INFINITY
import kotlin.math.abs

object Maps {
	val piece_values: Map<Piece, Double> = mapOf(
		Piece.WHITE_PAWN to 1.0,
		Piece.WHITE_KNIGHT to 3.0,
		Piece.WHITE_BISHOP to 3.0,
		Piece.WHITE_ROOK to 5.0,
		Piece.WHITE_QUEEN to 9.0,
		Piece.WHITE_KING to 0.0,

		Piece.BLACK_PAWN to -1.0,
		Piece.BLACK_KNIGHT to -3.0,
		Piece.BLACK_BISHOP to -3.0,
		Piece.BLACK_ROOK to -5.0,
		Piece.BLACK_QUEEN to -9.0,
		Piece.BLACK_KING to -0.0
	)
	val main: Map<Piece, Map<Square, Double>> = mapOf(
		Piece.WHITE_PAWN to mapOf(
			A8 to 0.0, B8 to 0.0, C8 to 0.0, D8 to 0.0, E8 to 0.0, F8 to 0.0, G8 to 0.0, H8 to 0.0,
			A7 to 3.5, B7 to 3.5, C7 to 3.5, D7 to 3.5, E7 to 3.5, F7 to 3.5, G7 to 3.5, H7 to 3.5,
			A6 to 0.2, B6 to 1.2, C6 to 1.7, D6 to 2.2, E6 to 2.2, F6 to 1.7, G6 to 1.2, H6 to 0.2,
			A5 to 0.2, B5 to 1.2, C5 to 1.7, D5 to 2.2, E5 to 2.2, F5 to 1.7, G5 to 1.2, H5 to 0.2,
			A4 to 0.1, B4 to 1.0, C4 to 1.5, D4 to 2.0, E4 to 2.0, F4 to 1.5, G4 to 1.0, H4 to 0.1,
			A3 to 0.0, B3 to 0.5, C3 to 1.0, D3 to 1.5, E3 to 1.5, F3 to 1.0, G3 to 0.5, H3 to 0.0,
			A2 to 0.0, B2 to 0.0, C2 to 0.0, D2 to 0.0, E2 to 0.0, F2 to 0.0, G2 to 0.0, H2 to 0.0,
			A1 to 0.0, B1 to 0.0, C1 to 0.0, D1 to 0.0, E1 to 0.0, F1 to 0.0, G1 to 0.0, H1 to 0.0,
		),
		Piece.WHITE_KNIGHT to mapOf(
			A8 to 0.3, B8 to 0.3, C8 to 0.3, D8 to 0.3, E8 to 0.3, F8 to 0.3, G8 to 0.3, H8 to 0.3,
			A7 to 0.4, B7 to 0.4, C7 to 0.9, D7 to 0.9, E7 to 0.9, F7 to 0.9, G7 to 0.4, H7 to 0.4,
			A6 to 0.5, B6 to 1.0, C6 to 1.2, D6 to 1.0, E6 to 1.0, F6 to 1.2, G6 to 1.0, H6 to 0.5,
			A5 to 0.4, B5 to 0.9, C5 to 0.9, D5 to 1.4, E5 to 1.4, F5 to 0.9, G5 to 0.9, H5 to 0.4,
			A4 to 0.3, B4 to 0.8, C4 to 0.8, D4 to 1.3, E4 to 1.3, F4 to 0.8, G4 to 0.8, H4 to 0.3,
			A3 to 0.2, B3 to 0.7, C3 to 0.9, D3 to 0.7, E3 to 0.7, F3 to 0.9, G3 to 0.7, H3 to 0.2,
			A2 to 0.1, B2 to 0.1, C2 to 0.6, D2 to 0.6, E2 to 0.6, F2 to 0.6, G2 to 0.6, H2 to 0.1,
			A1 to 0.0, B1 to 0.0, C1 to 0.0, D1 to 0.0, E1 to 0.0, F1 to 0.0, G1 to 0.0, H1 to 0.0,
		),
		Piece.WHITE_BISHOP to mapOf(
			A8 to 0.3, B8 to 0.4, C8 to 0.5, D8 to 0.6, E8 to 0.6, F8 to 0.5, G8 to 0.4, H8 to 0.3,
			A7 to 0.4, B7 to 0.6, C7 to 0.9, D7 to 0.9, E7 to 0.9, F7 to 0.9, G7 to 0.6, H7 to 0.4,
			A6 to 0.4, B6 to 1.0, C6 to 1.0, D6 to 1.2, E6 to 1.2, F6 to 1.0, G6 to 1.0, H6 to 0.5,
			A5 to 0.4, B5 to 0.9, C5 to 1.1, D5 to 1.4, E5 to 1.4, F5 to 1.1, G5 to 0.9, H5 to 0.4,
			A4 to 0.3, B4 to 0.8, C4 to 1.0, D4 to 1.3, E4 to 1.3, F4 to 1.0, G4 to 0.8, H4 to 0.3,
			A3 to 0.2, B3 to 0.7, C3 to 0.9, D3 to 0.9, E3 to 0.9, F3 to 0.7, G3 to 0.7, H3 to 0.2,
			A2 to 0.1, B2 to 0.3, C2 to 0.6, D2 to 0.6, E2 to 0.6, F2 to 0.6, G2 to 0.3, H2 to 0.1,
			A1 to 0.0, B1 to 0.1, C1 to 0.2, D1 to 0.3, E1 to 0.3, F1 to 0.2, G1 to 0.1, H1 to 0.0,
		),
		Piece.WHITE_ROOK to mapOf(
			A8 to 0.3, B8 to 0.3, C8 to 0.3, D8 to 0.3, E8 to 0.3, F8 to 0.3, G8 to 0.3, H8 to 0.3,
			A7 to 0.4, B7 to 0.4, C7 to 0.4, D7 to 0.4, E7 to 0.4, F7 to 0.4, G7 to 0.4, H7 to 0.4,
			A6 to 0.5, B6 to 1.0, C6 to 1.5, D6 to 1.5, E6 to 1.5, F6 to 1.5, G6 to 1.0, H6 to 0.5,
			A5 to 0.4, B5 to 0.9, C5 to 1.4, D5 to 2.4, E5 to 2.4, F5 to 1.4, G5 to 0.9, H5 to 0.4,
			A4 to 0.3, B4 to 0.8, C4 to 1.3, D4 to 2.3, E4 to 2.3, F4 to 1.3, G4 to 0.8, H4 to 0.3,
			A3 to 0.2, B3 to 0.7, C3 to 1.2, D3 to 1.2, E3 to 1.2, F3 to 1.2, G3 to 0.7, H3 to 0.2,
			A2 to 0.1, B2 to 0.1, C2 to 0.1, D2 to 0.1, E2 to 0.1, F2 to 0.1, G2 to 0.1, H2 to 0.1,
			A1 to 0.0, B1 to 0.0, C1 to 0.0, D1 to 0.0, E1 to 0.0, F1 to 0.0, G1 to 0.0, H1 to 0.0,
		),
		Piece.WHITE_QUEEN to mapOf(
			A8 to 0.3, B8 to 0.4, C8 to 0.5, D8 to 0.6, E8 to 0.6, F8 to 0.5, G8 to 0.4, H8 to 0.3,
			A7 to 0.4, B7 to 0.6, C7 to 0.9, D7 to 0.9, E7 to 0.9, F7 to 0.9, G7 to 0.6, H7 to 0.4,
			A6 to 0.4, B6 to 1.0, C6 to 1.0, D6 to 1.2, E6 to 1.2, F6 to 1.0, G6 to 1.0, H6 to 0.5,
			A5 to 0.4, B5 to 0.9, C5 to 1.1, D5 to 1.4, E5 to 1.4, F5 to 1.1, G5 to 0.9, H5 to 0.4,
			A4 to 0.3, B4 to 0.8, C4 to 1.0, D4 to 1.3, E4 to 1.3, F4 to 1.0, G4 to 0.8, H4 to 0.3,
			A3 to 0.2, B3 to 0.7, C3 to 0.9, D3 to 0.9, E3 to 0.9, F3 to 0.7, G3 to 0.7, H3 to 0.2,
			A2 to 0.1, B2 to 0.3, C2 to 0.6, D2 to 0.6, E2 to 0.6, F2 to 0.6, G2 to 0.3, H2 to 0.1,
			A1 to 0.0, B1 to 0.1, C1 to 0.2, D1 to 0.3, E1 to 0.3, F1 to 0.2, G1 to 0.1, H1 to 0.0,
		),
		Piece.WHITE_KING to mapOf(
			A8 to 1.0, B8 to 1.0, C8 to 1.0, D8 to 1.0, E8 to 1.0, F8 to 1.0, G8 to 1.0, H8 to 1.0,
			A7 to 1.0, B7 to 1.0, C7 to 1.0, D7 to 1.0, E7 to 1.0, F7 to 1.0, G7 to 1.0, H7 to 1.0,
			A6 to 1.0, B6 to 1.0, C6 to 1.0, D6 to 1.0, E6 to 1.0, F6 to 1.0, G6 to 1.0, H6 to 1.0,
			A5 to 1.0, B5 to 1.0, C5 to 1.0, D5 to 1.0, E5 to 1.0, F5 to 1.0, G5 to 1.0, H5 to 1.0,
			A4 to 1.0, B4 to 1.0, C4 to 1.0, D4 to 1.0, E4 to 1.0, F4 to 1.0, G4 to 1.0, H4 to 1.0,
			A3 to 1.0, B3 to 1.0, C3 to 1.0, D3 to 1.0, E3 to 1.0, F3 to 1.0, G3 to 1.0, H3 to 1.0,
			A2 to 2.0, B2 to 2.0, C2 to 2.0, D2 to 1.0, E2 to 1.0, F2 to 1.0, G2 to 2.0, H2 to 2.0,
			A1 to 3.0, B1 to 3.0, C1 to 3.0, D1 to 2.0, E1 to 1.0, F1 to 2.0, G1 to 3.0, H1 to 3.0,
		),
		Piece.BLACK_PAWN to mapOf(
			A1 to 0.0, B1 to 0.0, C1 to 0.0, D1 to 0.0, E1 to 0.0, F1 to 0.0, G1 to 0.0, H1 to 0.0,
			A2 to 3.5, B2 to 3.5, C2 to 3.5, D2 to 3.5, E2 to 3.5, F2 to 3.5, G2 to 3.5, H2 to 3.5,
			A3 to 0.2, B3 to 1.2, C3 to 1.7, D3 to 2.2, E3 to 2.2, F3 to 1.7, G3 to 1.2, H3 to 0.2,
			A4 to 0.2, B4 to 1.2, C4 to 1.7, D4 to 2.2, E4 to 2.2, F4 to 1.7, G4 to 1.2, H4 to 0.2,
			A5 to 0.1, B5 to 1.0, C5 to 1.5, D5 to 2.0, E5 to 2.0, F5 to 1.5, G5 to 1.0, H5 to 0.1,
			A6 to 0.0, B6 to 0.5, C6 to 1.0, D6 to 1.5, E6 to 1.5, F6 to 1.0, G6 to 0.5, H6 to 0.0,
			A7 to 0.0, B7 to 0.0, C7 to 0.0, D7 to 0.0, E7 to 0.0, F7 to 0.0, G7 to 0.0, H7 to 0.0,
			A8 to 0.0, B8 to 0.0, C8 to 0.0, D8 to 0.0, E8 to 0.0, F8 to 0.0, G8 to 0.0, H8 to 0.0,
		),
		Piece.BLACK_KNIGHT to mapOf(
			A1 to 0.3, B1 to 0.3, C1 to 0.3, D1 to 0.3, E1 to 0.3, F1 to 0.3, G1 to 0.3, H1 to 0.3,
			A2 to 0.4, B2 to 0.4, C2 to 0.9, D2 to 0.9, E2 to 0.9, F2 to 0.9, G2 to 0.4, H2 to 0.4,
			A3 to 0.5, B3 to 1.0, C3 to 1.2, D3 to 1.0, E3 to 1.0, F3 to 1.2, G3 to 1.0, H3 to 0.5,
			A4 to 0.4, B4 to 0.9, C4 to 0.9, D4 to 1.4, E4 to 1.4, F4 to 0.9, G4 to 0.9, H4 to 0.4,
			A5 to 0.3, B5 to 0.8, C5 to 0.8, D5 to 1.3, E5 to 1.3, F5 to 0.8, G5 to 0.8, H5 to 0.3,
			A6 to 0.2, B6 to 0.7, C6 to 0.9, D6 to 0.7, E6 to 0.7, F6 to 0.9, G6 to 0.7, H6 to 0.2,
			A7 to 0.1, B7 to 0.1, C7 to 0.6, D7 to 0.6, E7 to 0.6, F7 to 0.6, G7 to 0.6, H7 to 0.1,
			A8 to 0.0, B8 to 0.0, C8 to 0.0, D8 to 0.0, E8 to 0.0, F8 to 0.0, G8 to 0.0, H8 to 0.0,
		),
		Piece.BLACK_BISHOP to mapOf(
			A1 to 0.3, B1 to 0.4, C1 to 0.5, D1 to 0.6, E1 to 0.6, F1 to 0.5, G1 to 0.4, H1 to 0.3,
			A2 to 0.4, B2 to 0.6, C2 to 0.9, D2 to 0.9, E2 to 0.9, F2 to 0.9, G2 to 0.6, H2 to 0.4,
			A3 to 0.4, B3 to 1.0, C3 to 1.0, D3 to 1.2, E3 to 1.2, F3 to 1.0, G3 to 1.0, H3 to 0.5,
			A4 to 0.4, B4 to 0.9, C4 to 1.1, D4 to 1.4, E4 to 1.4, F4 to 1.1, G4 to 0.9, H4 to 0.4,
			A5 to 0.3, B5 to 0.8, C5 to 1.0, D5 to 1.3, E5 to 1.3, F5 to 1.0, G5 to 0.8, H5 to 0.3,
			A6 to 0.2, B6 to 0.7, C6 to 0.9, D6 to 0.9, E6 to 0.9, F6 to 0.7, G6 to 0.7, H6 to 0.2,
			A7 to 0.1, B7 to 0.3, C7 to 0.6, D7 to 0.6, E7 to 0.6, F7 to 0.6, G7 to 0.3, H7 to 0.1,
			A8 to 0.0, B8 to 0.1, C8 to 0.2, D8 to 0.3, E8 to 0.3, F8 to 0.2, G8 to 0.1, H8 to 0.0,
		),
		Piece.BLACK_ROOK to mapOf(
			A1 to 0.3, B1 to 0.3, C1 to 0.3, D1 to 0.3, E1 to 0.3, F1 to 0.3, G1 to 0.3, H1 to 0.3,
			A2 to 0.4, B2 to 0.4, C2 to 0.4, D2 to 0.4, E2 to 0.4, F2 to 0.4, G2 to 0.4, H2 to 0.4,
			A3 to 0.5, B3 to 1.0, C3 to 1.5, D3 to 1.5, E3 to 1.5, F3 to 1.5, G3 to 1.0, H3 to 0.5,
			A4 to 0.4, B4 to 0.9, C4 to 1.4, D4 to 2.4, E4 to 2.4, F4 to 1.4, G4 to 0.9, H4 to 0.4,
			A5 to 0.3, B5 to 0.8, C5 to 1.3, D5 to 2.3, E5 to 2.3, F5 to 1.3, G5 to 0.8, H5 to 0.3,
			A6 to 0.2, B6 to 0.7, C6 to 1.2, D6 to 1.2, E6 to 1.2, F6 to 1.2, G6 to 0.7, H6 to 0.2,
			A7 to 0.1, B7 to 0.1, C7 to 0.1, D7 to 0.1, E7 to 0.1, F7 to 0.1, G7 to 0.1, H7 to 0.1,
			A8 to 0.0, B8 to 0.0, C8 to 0.0, D8 to 0.0, E8 to 0.0, F8 to 0.0, G8 to 0.0, H8 to 0.0,
		),
		Piece.BLACK_QUEEN to mapOf(
			A1 to 0.3, B1 to 0.4, C1 to 0.5, D1 to 0.6, E1 to 0.6, F1 to 0.5, G1 to 0.4, H1 to 0.3,
			A2 to 0.4, B2 to 0.6, C2 to 0.9, D2 to 0.9, E2 to 0.9, F2 to 0.9, G2 to 0.6, H2 to 0.4,
			A3 to 0.4, B3 to 1.0, C3 to 1.0, D3 to 1.2, E3 to 1.2, F3 to 1.0, G3 to 1.0, H3 to 0.5,
			A4 to 0.4, B4 to 0.9, C4 to 1.1, D4 to 1.4, E4 to 1.4, F4 to 1.1, G4 to 0.9, H4 to 0.4,
			A5 to 0.3, B5 to 0.8, C5 to 1.0, D5 to 1.3, E5 to 1.3, F5 to 1.0, G5 to 0.8, H5 to 0.3,
			A6 to 0.2, B6 to 0.7, C6 to 0.9, D6 to 0.9, E6 to 0.9, F6 to 0.7, G6 to 0.7, H6 to 0.2,
			A7 to 0.1, B7 to 0.3, C7 to 0.6, D7 to 0.6, E7 to 0.6, F7 to 0.6, G7 to 0.3, H7 to 0.1,
			A8 to 0.0, B8 to 0.1, C8 to 0.2, D8 to 0.3, E8 to 0.3, F8 to 0.2, G8 to 0.1, H8 to 0.0,
		),
		Piece.BLACK_KING to mapOf(
			A1 to 3.0, B1 to 3.0, C1 to 3.0, D1 to 2.0, E1 to 1.0, F1 to 2.0, G1 to 3.0, H1 to 3.0,
			A2 to 2.0, B2 to 2.0, C2 to 1.0, D2 to 1.0, E2 to 1.0, F2 to 1.0, G2 to 2.0, H2 to 2.0,
			A3 to 1.0, B3 to 1.0, C3 to 1.0, D3 to 1.0, E3 to 1.0, F3 to 1.0, G3 to 1.0, H3 to 1.0,
			A4 to 1.0, B4 to 1.0, C4 to 1.0, D4 to 1.0, E4 to 1.0, F4 to 1.0, G4 to 1.0, H4 to 1.0,
			A5 to 1.0, B5 to 1.0, C5 to 1.0, D5 to 1.0, E5 to 1.0, F5 to 1.0, G5 to 1.0, H5 to 1.0,
			A6 to 1.0, B6 to 1.0, C6 to 1.0, D6 to 1.0, E6 to 1.0, F6 to 1.0, G6 to 1.0, H6 to 1.0,
			A7 to 1.0, B7 to 1.0, C7 to 1.0, D7 to 1.0, E7 to 1.0, F7 to 1.0, G7 to 1.0, H7 to 1.0,
			A8 to 1.0, B8 to 1.0, C8 to 1.0, D8 to 1.0, E8 to 1.0, F8 to 1.0, G8 to 1.0, H8 to 1.0,
		),
	)
}

fun evaluate(
	board: Board
): Double {
	when {
		board.isDraw -> return 0.0
		board.isMated && board.sideToMove == Side.BLACK -> return POSITIVE_INFINITY
		board.isMated && board.sideToMove == Side.WHITE -> return NEGATIVE_INFINITY
	}
	var score: Double = 0.0
	for (piece: Piece in Piece.allPieces) {
		for (square: Square? in board.getPieceLocation(
			piece
		)) {
			if (square == null) {
				continue
			}

			// material, adjusted to position
			score += (Maps.piece_values[piece] ?: 0.0) + (Maps.main[piece]?.get(square) ?: 0.0)
		}
	}

	// attacked squares
	for (square: Square in Square.entries) {
		val attackedWhite: Double = board.squareAttackedBy(square, Side.WHITE).countOneBits().toDouble()
		val attackedBlack: Double = board.squareAttackedBy(square, Side.BLACK).countOneBits().toDouble()

		// general / moving
		score += attackedWhite / 16.0
		score -= attackedBlack / 16.0

		// more than opponent / attacking
		when {
			(attackedWhite > attackedBlack) -> {
				score += abs((Maps.piece_values[board.getPiece(square)] ?: 0.0) / 2.0)
			}

			(attackedBlack > attackedWhite) -> {
				score -= abs((Maps.piece_values[board.getPiece(square)] ?: 0.0) / 2.0)
			}
		}

	}

	return score
}

fun generate(board: Board, depth: Int = 0, alpha: Double = NEGATIVE_INFINITY, beta: Double = POSITIVE_INFINITY, returnMove: Boolean = true): Any? {
	// https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
	if (depth == 0 || board.isDraw || board.isMated) {
		return when (returnMove) {
			true -> Unit
			false -> evaluate(board)
		}
	}
	var score: Double = 0.0
	var bestMove: Move? = null
	var alpha: Double = alpha
	var beta: Double = beta
	when (board.sideToMove) {
		Side.WHITE -> {
			// Maximizing
			score = NEGATIVE_INFINITY
			for (move: Move in board.legalMoves()) {
				board.doMove(move)
				val generatedScore: Double = generate(board, depth - 1, alpha, beta, false) as Double
				if (generatedScore > score) {
					bestMove = move
					score = generatedScore
				}
				board.undoMove()
				if (score >= beta) {
					break
				}
				alpha = maxOf(alpha, score)
			}
		}

		Side.BLACK -> {
			// Minimizing
			score = POSITIVE_INFINITY
			for (move: Move in board.legalMoves()) {
				board.doMove(move)
				val generatedScore: Double = generate(board, depth - 1, alpha, beta, false) as Double
				if (generatedScore < score) {
					bestMove = move
					score = generatedScore
				}
				board.undoMove()
				if (score <= alpha) {
					break
				}
				beta = minOf(beta, score)
			}
		}
	}
	return when (returnMove) {
		true -> bestMove
		false -> score
	}
}