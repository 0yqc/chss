package org.yqc.chss

import kotlin.math.round
import kotlin.time.*

class ProgressBar(val len: Double, val width: Int = 60) {
	val timeSource: TimeSource = TimeSource.Monotonic
	val timeStart: TimeMark = timeSource.markNow()
	val step: Double = width.toDouble() / len
	var currentStep: Double = 0.0
	var currentPrinted: Int = 0

	init {
		print("[${" ".repeat(width)}] 0% | 0s /")
	}

	fun next(n: Double = 1.0) {
		val duration: Duration = timeStart.elapsedNow()
		currentStep += n
		currentPrinted = (step * currentStep).toInt()
		print("\\x1B[1K\r[${"#".repeat(currentPrinted)}${" ".repeat(width - currentPrinted)}] ${round(currentStep / len * 100).toInt()}% | ${duration.inWholeSeconds}s / ${(duration / currentStep * len).inWholeSeconds}s")
	}
}