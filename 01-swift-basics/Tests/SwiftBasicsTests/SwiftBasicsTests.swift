import Testing
@testable import SwiftBasics

@Test func greetWorks() {
    #expect(BasicsExercises.greet(name: "David") == "Hello, David!")
}

@Test func parseScore() {
    #expect(BasicsExercises.parseScore("42", default: 0) == 42)
    #expect(BasicsExercises.parseScore("nope", default: 7) == 7)
}

@Test func frequencies() {
    #expect(BasicsExercises.wordFrequencies(in: ["Hi", "hi", " ", "Yo"]) == ["hi": 2, "yo": 1])
}

@Test func temperature() {
    let c = MeasurementSample(value: 0, unit: .celsius)
    #expect(BasicsExercises.converted(c, to: .fahrenheit).value == 32)
}
