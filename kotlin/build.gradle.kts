plugins {
	kotlin("jvm") version "2.2.20"
	application
}

group = "org.example"
version = "1.0-SNAPSHOT"

repositories {
	mavenCentral()
}

dependencies {
	implementation("io.github.cvb941:kchesslib:1.0.4")
}

application {
	mainClass = "org.yqc.chss.MainKt"
}

kotlin {
	jvmToolchain(21)
}