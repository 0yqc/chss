package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.move.*
import kotlin.Double.Companion.NEGATIVE_INFINITY
import kotlin.Double.Companion.POSITIVE_INFINITY

fun evaluate(board: Board): Double {
	return 0.0
}

fun generate(
	board: Board,
	depth: Int = 4,
	alpha: Double = POSITIVE_INFINITY,
	beta: Double = NEGATIVE_INFINITY,
	returnMove: Boolean = true
): Any {
	// https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
	if (depth == 0 || board.isDraw || board.isMated) {
		return evaluate(board)
	}
	var score: Double = 0.0
	lateinit var bestMove: Move
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