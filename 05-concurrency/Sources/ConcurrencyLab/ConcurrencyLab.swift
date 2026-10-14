public actor ScoreBoard: Sendable {
    private var scores: [String: Int] = [:]

    public init() {}

    public func setScore(_ score: Int, for player: String) {
        scores[player] = score
    }

    public func score(for player: String) -> Int? {
        scores[player]
    }

// MARK: - TODO: Actor isolation
/*
 Goal:
 Add a method that increments a player's score safely inside the actor.

 Steps:
 1. Implement `addPoints(_:to:)` on ScoreBoard.
 2. If player missing, start from 0.

 Hints:
 - All mutable state stays inside the actor.

 Acceptance criteria:
 - Concurrent increments do not data-race (Swift 6 default isolation).

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/
 - https://developer.apple.com/documentation/swift/actor
*/

    // public func addPoints(_ points: Int, to player: String) { fatalError("TODO") }
}

public enum AsyncExercises {
// MARK: - TODO: async/await + TaskGroup
/*
 Goal:
 Fetch multiple fake resources concurrently and collect results.

 Steps:
 1. Implement `loadAll(ids:)` using `withTaskGroup`.
 2. Each child calls `fakeFetch(id:)` below.
 3. Return results sorted by id.

 Hints:
 - `fakeFetch` already exists — reuse it.
 - Prefer structured concurrency over detached tasks.

 Acceptance criteria:
 - Order of returned array is sorted by id regardless of completion order.

 Docs:
 - https://developer.apple.com/documentation/swift/taskgroup
 - https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/
*/

    public static func fakeFetch(id: String) async -> (id: String, value: Int) {
        try? await Task.sleep(for: .milliseconds(10))
        return (id, id.count)
    }

    // public static func loadAll(ids: [String]) async -> [(id: String, value: Int)] { fatalError("TODO") }
}
