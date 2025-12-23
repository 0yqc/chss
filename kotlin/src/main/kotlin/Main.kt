package org.yqc.chss

import com.github.bhlangonijr.chesslib.*
import com.github.bhlangonijr.chesslib.move.*
import kotlin.time.Duration
import kotlin.time.Duration.Companion.seconds
import kotlin.time.measureTimedValue

fun main() {
	val board: Board = Board()

	val players: Map<Side, String> = mapOf(
		Side.WHITE to "chss",
		Side.BLACK to "chss"
	)

	var depth: Int = 6 // initial depth; only whole number will be taken for the real depth
	val timeIncr: Duration? = 5.seconds // time to increase depth by 1 when under twice; null to disable
	val timeDecr: Duration? = 15.seconds // time to decrease depth by 1 when over once; null to disable
	// NOTE: aren't hard limits, often will be over/under

	var depthAdj: Double = 0.0

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
					println("Move: $move")
					println("Score: ${evaluate(board)}")
					println()
				}
			}

			"chss" -> {
				val (move: Move, time: Duration) = measureTimedValue {
					generate(board, depth = depth) as Move
				}
				if (move == Unit) {
					error("Stalemate, Checkmate or Depth < 1")
				}
				// only do something if twice too low/high
				board.doMove(move)
				when {
					(timeDecr != null && time > timeDecr) -> depthAdj = -1.0
					(timeIncr != null && time < timeIncr) -> depthAdj += 0.5
					else -> depthAdj = 0.0
				}
				println()
				println("Move: $move")
				println("Time: ${time.inWholeSeconds}s")
				println("Depth: $depth (${if (depthAdj >= 0) "+$depthAdj" else depthAdj})")
				println("Score: ${evaluate(board)}")
				println()
				when {
					depthAdj >= 1.0 -> {
						depth++
						depthAdj = 0.0
					}

					depthAdj <= -1.0 -> {
						depth--
						depthAdj = 0.0
					}
				}
				depth.coerceAtLeast(1)
			}
		}
	}
}