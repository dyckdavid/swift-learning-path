/// Project 01 — Swift basics: types, optionals, collections.
/// Open this folder in Xcode (File → Open → Package.swift) or use `swift build` / `swift test`.

public enum TemperatureUnit: String, Sendable {
    case celsius
    case fahrenheit
}

public struct MeasurementSample: Equatable, Sendable {
    public var value: Double
    public var unit: TemperatureUnit

    public init(value: Double, unit: TemperatureUnit) {
        self.value = value
        self.unit = unit
    }
}

public enum BasicsExercises {
    /// Starter helper used by tests — keep compiling while you fill in TODOs.
    public static func greet(name: String) -> String {
        "Hello, \(name)!"
    }

// MARK: - TODO: Optionals and nil-coalescing
/*
 Goal:
 Parse an optional Int from a String and provide a default.

 Steps:
 1. Implement `parseScore(_:default:)` below (uncomment and fill in).
 2. Return the Int value when parsing succeeds; otherwise return `defaultValue`.
 3. Call your function from the CLI target for a quick smoke check.

 Hints:
 - Use `Int(_:)` which returns `Int?`.
 - Prefer `??` or `guard let` — both are fine.

 Acceptance criteria:
 - `parseScore("42", default: 0) == 42`
 - `parseScore("abc", default: 0) == 0`

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/optionals/
*/

    // public static func parseScore(_ text: String, default defaultValue: Int) -> Int {
    //     fatalError("TODO")
    // }

// MARK: - TODO: Collections
/*
 Goal:
 Build a frequency dictionary from an array of words (case-insensitive).

 Steps:
 1. Implement `wordFrequencies(in:)` returning `[String: Int]`.
 2. Normalize keys with `lowercased()`.
 3. Ignore empty strings after trimming whitespace.

 Hints:
 - Start with `[:]` and mutate counts, or use `reduce(into:)`.
 - `trimmingCharacters(in: .whitespacesAndNewlines)` is useful.

 Acceptance criteria:
 - `wordFrequencies(in: ["Hi", "hi", " ", "Yo"]) == ["hi": 2, "yo": 1]`

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collectiontypes/
*/

    // public static func wordFrequencies(in words: [String]) -> [String: Int] {
    //     fatalError("TODO")
    // }

// MARK: - TODO: Convert temperatures
/*
 Goal:
 Convert a MeasurementSample between Celsius and Fahrenheit.

 Steps:
 1. Implement `converted(_:to:)`.
 2. If units already match, return the input unchanged.
 3. C→F: `c * 9/5 + 32`. F→C: `(f - 32) * 5/9`.

 Hints:
 - Keep the result in a new `MeasurementSample`.

 Acceptance criteria:
 - Converting 0°C to Fahrenheit yields 32.
 - Converting 32°F to Celsius yields 0.

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/
*/

    // public static func converted(_ sample: MeasurementSample, to unit: TemperatureUnit) -> MeasurementSample {
    //     fatalError("TODO")
    // }
}
