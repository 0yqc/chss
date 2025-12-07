package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.move.*

fun main() {
	val board: Board = Board()
	val players: Map<Side, String> = mapOf(
		Side.WHITE to "human",
		Side.BLACK to "chss"
	)
	while (!board.isDraw && !board.isMated) {
		when (players[board.sideToMove]) {
			"human" -> {
				var moved: Boolean = false
				while (!moved) {
					moved = true
					print("Move (algebraic notation / UCI): ")
					val inp: String = readln()
					try {
						board.doMove(inp)
					} catch (_: MoveConversionException) {
						moved = false
					}
				}
			}

			"chss" -> {
				board.doMove(generate(board) as Move)
			}
		}
		println()
		println(board)
		println()
	}
}