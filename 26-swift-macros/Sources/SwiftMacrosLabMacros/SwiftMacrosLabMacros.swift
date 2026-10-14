import SwiftCompilerPlugin
import SwiftSyntax
import SwiftSyntaxBuilder
import SwiftSyntaxMacros

/// Freestanding expression macro `#stringify(expr)` → tuple of (value, source code string).
public struct StringifyMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) throws -> ExprSyntax {
        // MARK: - TODO: Implement #stringify
        /*
         Goal:
         Return an expression that creates a tuple (value, "source").

         Steps:
         1. Read the first argument expression from `node`.
         2. Use the argument description for the string side.
         3. Classic implementation returns: `( <arg>, "<arg>" )` as ExprSyntax.

         Hints:
         - Apple sample / SE-style stringify is the usual tutorial macro.
         - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/

         Acceptance criteria:
         - `#stringify(1 + 2)` expands such that `.1` contains `1 + 2`.

         Docs:
         - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/
         - https://developer.apple.com/documentation/swift/macros
        */
        // Starter: compile-safe placeholder expansion so the package can build before you implement.
        return ExprSyntax(stringLiteral: #"(0, "TODO")"#)
    }
}

@main
struct SwiftMacrosLabPlugin: CompilerPlugin {
    let providingMacros: [Macro.Type] = [StringifyMacro.self]
}
