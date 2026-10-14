import Testing
import SwiftMacrosLab

@Test func stringifyCompiles() {
    let pair = #stringify(2)
    #expect(pair.0 == 2)
    #expect(pair.1.contains("2"))
}
