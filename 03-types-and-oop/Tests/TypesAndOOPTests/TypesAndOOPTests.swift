import Testing
@testable import TypesAndOOP

@Test func counterIncrements() {
    let c = Counter()
    c.increment()
    #expect(c.value == 1)
}
