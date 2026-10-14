public struct Point: Equatable, Sendable {
    public var x: Double
    public var y: Double
    public init(x: Double, y: Double) { self.x = x; self.y = y }
}

public enum Shape: Equatable, Sendable {
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
}

public final class Counter: @unchecked Sendable {
    public private(set) var value: Int
    public init(value: Int = 0) { self.value = value }
    public func increment() { value += 1 }
}

public enum TypeExercises {
// MARK: - TODO: Enum methods & computed properties
/*
 Goal:
 Add area computation for Shape.

 Steps:
 1. Implement `area(of:)` for circle (πr²) and rectangle (w×h).
 2. Use `Double.pi`.

 Hints:
 - Switch must be exhaustive.

 Acceptance criteria:
 - Circle r=1 → π
 - Rectangle 3×4 → 12

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/enumerations/
*/

    // public static func area(of shape: Shape) -> Double { fatalError("TODO") }

// MARK: - TODO: Value vs reference semantics
/*
 Goal:
 Demonstrate copying a Point vs sharing a Counter.

 Steps:
 1. Implement `moved(_ :by:)` returning a new Point offset by dx/dy without mutating the input.
 2. Implement `bumpTwice(_:)` that increments the same Counter instance twice and returns its value.

 Hints:
 - Structs copy; classes share identity.

 Acceptance criteria:
 - Point(0,0) moved by (1,2) → (1,2) and original stays (0,0).

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/
*/

    // public static func moved(_ point: Point, by delta: Point) -> Point { fatalError("TODO") }
    // public static func bumpTwice(_ counter: Counter) -> Int { fatalError("TODO") }
}
