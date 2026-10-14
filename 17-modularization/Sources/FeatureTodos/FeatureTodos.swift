import Core

public enum TodoFeature {
    public static func sample() -> [TodoDTO] {
        [TodoDTO(title: "Learn modules")]
    }

// MARK: - TODO: Feature API on top of Core
/*
 Goal:
 Add a filter helper that belongs in the feature module but uses Core DTOs.

 Steps:
 1. Implement `openTodos(in:)` returning items whose titles are non-empty.
 2. Do not invent networking here — keep the feature pure.

 Hints:
 - Depend only on Core.

 Acceptance criteria:
 - Filters out empty titles.

 Docs:
 - https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages
*/

    // public static func openTodos(in items: [TodoDTO]) -> [TodoDTO] { fatalError("TODO") }
}
