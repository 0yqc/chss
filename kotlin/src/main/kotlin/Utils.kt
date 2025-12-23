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
		currentStep += n
		currentPrinted = (step * currentStep).toInt()
		val durationFromStart: Duration = timeStart.elapsedNow()
		val expectionAll: Duration = durationFromStart / currentStep * len
		print("\\x1B[1K\r[${"#".repeat(currentPrinted)}${" ".repeat(width - currentPrinted)}] ${round(currentStep / len * 100).toInt()}% | ${durationFromStart.inWholeSeconds}s / ${expectionAll.inWholeSeconds}s")
	}
}