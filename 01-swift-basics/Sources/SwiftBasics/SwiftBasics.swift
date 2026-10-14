import Foundation

/// Project 01 — solutions
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
    public static func greet(name: String) -> String { "Hello, \(name)!" }

    public static func parseScore(_ text: String, default defaultValue: Int) -> Int {
        Int(text) ?? defaultValue
    }

    public static func wordFrequencies(in words: [String]) -> [String: Int] {
        var result: [String: Int] = [:]
        for word in words {
            let key = word.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
            guard !key.isEmpty else { continue }
            result[key, default: 0] += 1
        }
        return result
    }

    public static func converted(_ sample: MeasurementSample, to unit: TemperatureUnit) -> MeasurementSample {
        guard sample.unit != unit else { return sample }
        switch (sample.unit, unit) {
        case (.celsius, .fahrenheit):
            return MeasurementSample(value: sample.value * 9 / 5 + 32, unit: .fahrenheit)
        case (.fahrenheit, .celsius):
            return MeasurementSample(value: (sample.value - 32) * 5 / 9, unit: .celsius)
        default:
            return sample
        }
    }
}
