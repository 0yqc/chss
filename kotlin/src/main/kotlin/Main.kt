package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.move.*
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds
import kotlin.time.measureTimedValue

fun main() {
	val board: Board = Board()

	val players: Map<Side, String> = mapOf(
		Side.WHITE to "human",
		Side.BLACK to "chss"
	)

	var depth = 5 // initial depth
	val timeMin = 2.seconds // time to increase depth when under
	val timeMax = 30.seconds // time to decrease depth when over
	// NOTE: aren't hard limits, often will be over/under

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
				val (move: Move, time: Duration) = measureTimedValue {
					generate(board, depth = depth) as Move? ?: error("No best move found, possibly a check- or stalemate.")
				}
				val depthAdj = when {
					(time > timeMax) -> - 1
					(time < timeMin) -> 1
					else -> 0
				}
				board.doMove(move)
				println()
				println(board)
				println("Move: $move")
				println("Time: $time")
				println("Depth: $depth (+ $depthAdj)")
				depth += depthAdj
				println()
			}
		}
	}
}