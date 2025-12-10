package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.move.*

fun main() {
	val board: Board = Board()
	val players: Map<Side, String> = mapOf(
		Side.WHITE to "chss",
		Side.BLACK to "human"
	)
	moveLoop@ while (!board.isDraw && !board.isMated) {
		when (players[board.sideToMove]) {
			"human" -> {
				var moved: Boolean = false
				while (!moved) {
					moved = true
					print("Move (algebraic notation / UCI): ")
					val move: String = readln()
					when (move) {
						"undo" -> {
							board.undoMove()
							board.undoMove()
							continue@moveLoop
						}
					}
					try {
						board.doMove(move)
					} catch (e: MoveConversionException) {
						println(e)
						moved = false
						continue
					}
					println()
					println(board)
					println("Move: $move")
					println()
				}
			}

			"chss" -> {
				val move: Move = generate(board, depth = 5) as Move? ?: error("No best move found")
				board.doMove(move)
				println()
				println(board)
				println("Move: $move")
				println()
			}
		}
	}
}