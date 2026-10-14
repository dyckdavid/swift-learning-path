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
    public static func area(of shape: Shape) -> Double {
        switch shape {
        case .circle(let r): return Double.pi * r * r
        case .rectangle(let w, let h): return w * h
        }
    }

    public static func moved(_ point: Point, by delta: Point) -> Point {
        Point(x: point.x + delta.x, y: point.y + delta.y)
    }

    public static func bumpTwice(_ counter: Counter) -> Int {
        counter.increment(); counter.increment(); return counter.value
    }
}
