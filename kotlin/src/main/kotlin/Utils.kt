package org.yqc.chss

import kotlin.math.round

class ProgressBar(val len: Double, val width: Int = 60) {
	val step: Double = width.toDouble() / len
	var currentStep: Double = 0.0
	var currentPrinted: Int = 0

	fun next(n: Double = 1.0) {
		currentStep += n
		currentPrinted = (step * currentStep).toInt()
		print("\\x1B[1K\r[${"#".repeat(currentPrinted)}${" ".repeat(width - currentPrinted)}] ${round(currentStep / len * 100).toInt()}%")
	}
}