package org.yqc.chss

import com.github.bhlangonijr.chesslib.*

fun main() {
	val board: Board = Board()
	board.loadFromFen("r3k2r/p3bppp/q3p3/2pnP3/2Np4/P7/1P2QPPP/R1B2KR1 w kq - 0 15")
	println(generate(board, depth = 5))

	println(evaluate(board))
}