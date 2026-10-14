import Testing
@testable import SwiftBasics

@Test func greetWorks() {
    #expect(BasicsExercises.greet(name: "David") == "Hello, David!")
}

// Uncomment as you implement TODOs:
// @Test func parseScore() {
//     #expect(BasicsExercises.parseScore("42", default: 0) == 42)
//     #expect(BasicsExercises.parseScore("nope", default: 7) == 7)
// }
