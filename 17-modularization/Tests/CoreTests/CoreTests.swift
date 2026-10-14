import Testing
import Core

@Test func dtoIdentity() {
    let a = TodoDTO(title: "A")
    #expect(a.title == "A")
}
