package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import kotlin.time.*
import kotlin.math.abs

fun main() {
	val board: Board = Board()

	while (true) {
		println(evaluateAnalyze(board))
		print("Move: ")
		board.doMove(readln())
	}
}

fun evaluateAnalyze(board: Board): Double {
	val timeSource: TimeSource = TimeSource.Monotonic
	val start = timeSource.markNow()
	var scorePosMaterial: Double = 0.0
	var scorePawnStructure: Double = 0.0
	var scoreMobility: Double = 0.0
	var scoreAttacking: Double = 0.0
	val nPawns: Int = board.getBitboard(Piece.WHITE_PAWN).countOneBits() + board.getBitboard(Piece.BLACK_PAWN).countOneBits()
	// knights are stronger with more pawns, bishops stronger with fewer pawns
	val pieceValues: Map<Piece, Double> = mapOf(
		Piece.WHITE_PAWN to 1.0,
		Piece.WHITE_KNIGHT to 2.0 + nPawns / 8.0,
		Piece.WHITE_BISHOP to 4.0 - nPawns / 8.0,
		Piece.WHITE_ROOK to 5.0,
		Piece.WHITE_QUEEN to 9.0,
		Piece.WHITE_KING to 0.0,

		Piece.BLACK_PAWN to -1.0,
		Piece.BLACK_KNIGHT to -2.0 - nPawns / 8.0,
		Piece.BLACK_BISHOP to -4.0 + nPawns / 8.0,
		Piece.BLACK_ROOK to -5.0,
		Piece.BLACK_QUEEN to -9.0,
		Piece.BLACK_KING to -0.0
	)
	println("Init: ${start.elapsedNow()}")
	for (piece: Piece in Piece.allPieces) {
		for (square: Square? in board.getPieceLocation(piece)) {
			if (square == null) {
				continue
			}

			// material, adjusted to position
			scorePosMaterial += (pieceValues[piece] ?: 0.0) + (Maps.main[piece]?.get(square) ?: 0.0)

			// pawn structure
			// 0.25 if pawn is protected once, no more
			scorePawnStructure += when {
				(piece == Piece.WHITE_PAWN && board.squareAttackedByPieceType(square, Side.WHITE, PieceType.PAWN) != 0L) -> 0.25
				(piece == Piece.BLACK_PAWN && board.squareAttackedByPieceType(square, Side.BLACK, PieceType.PAWN) != 0L) -> -0.25
				else -> 0.0
			}
		}
	}
	println("Piece/Square Loop: ${start.elapsedNow()}")

	// attacked squares
	for (square: Square in Square.entries) {
		val attackedWhiteCount: Double = board.squareAttackedBy(square, Side.WHITE).countOneBits().toDouble()
		val attackedBlackCount: Double = board.squareAttackedBy(square, Side.BLACK).countOneBits().toDouble()

		// general / moving
		scoreMobility += attackedWhiteCount / 32.0
		scoreMobility -= attackedBlackCount / 32.0

		// more than opponent / attacking
		when {
			(attackedWhiteCount > attackedBlackCount) -> {
				scoreAttacking += abs((pieceValues[board.getPiece(square)] ?: 0.0) / 4.0)
			}

			(attackedBlackCount > attackedWhiteCount) -> {
				scoreAttacking -= abs((pieceValues[board.getPiece(square)] ?: 0.0) / 4.0)
			}
		}
	}
	println("Square Loop: ${start.elapsedNow()}")
	println("Material: $scorePosMaterial\nPawn Structure: $scorePawnStructure\nMobillity: $scoreMobility\nAttacking: $scoreAttacking")
	return scorePosMaterial + scorePawnStructure + scoreMobility + scoreAttacking
}