import Testing
import SwiftMacrosLab

@Test func stringifyCompiles() {
    let pair = #stringify(2)
    // Starter macro returns placeholder (0, "TODO") until you implement expansion.
    #expect(pair.0 == 0)
}
