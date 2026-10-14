public enum MathOps {
    public static func identity(_ value: Int) -> Int { value }

// MARK: - TODO: Higher-order functions
/*
 Goal:
 Implement map/filter/reduce-style helpers without calling the stdlib versions for practice (or call them — your choice; document which).

 Steps:
 1. Implement `squaredEvens(in:)` → squares of even numbers, preserving order.
 2. Implement `sum(of:using:)` that reduces `[Int]` with a closure `(Int, Int) -> Int`.

 Hints:
 - `filter` then `map` is fine.
 - Default the sum operator to `+` via a default parameter if you like.

 Acceptance criteria:
 - `squaredEvens(in: [1,2,3,4]) == [4, 16]`
 - `sum(of: [1,2,3], using: +) == 6`

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/
*/

    // public static func squaredEvens(in values: [Int]) -> [Int] { fatalError("TODO") }
    // public static func sum(of values: [Int], using combine: (Int, Int) -> Int) -> Int { fatalError("TODO") }

// MARK: - TODO: Escaping closures & trailing syntax
/*
 Goal:
 Run an async-looking completion on a success path (still synchronous for this exercise).

 Steps:
 1. Implement `perform(success:failure:)` that calls `success("ok")` when `shouldSucceed` is true, else `failure`.
 2. Mark closures `@escaping` if stored; here they are called immediately so escaping is optional — use it if you store them.

 Hints:
 - Practice trailing-closure call sites in the CLI.

 Acceptance criteria:
 - Success path returns the string from the success closure to the caller.

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/
*/

    // Toggle in CLI/tests when implementing the TODO below.
    nonisolated(unsafe) public static var shouldSucceed: Bool = true
    // public static func perform(success: (String) -> String, failure: () -> String) -> String { fatalError("TODO") }
}
