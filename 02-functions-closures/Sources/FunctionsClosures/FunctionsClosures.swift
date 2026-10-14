public enum MathOps {
    public static func identity(_ value: Int) -> Int { value }

    public static func squaredEvens(in values: [Int]) -> [Int] {
        values.filter { $0.isMultiple(of: 2) }.map { $0 * $0 }
    }

    public static func sum(of values: [Int], using combine: (Int, Int) -> Int) -> Int {
        values.reduce(0, combine)
    }

    nonisolated(unsafe) public static var shouldSucceed: Bool = true

    public static func perform(success: (String) -> String, failure: () -> String) -> String {
        shouldSucceed ? success("ok") : failure()
    }
}
