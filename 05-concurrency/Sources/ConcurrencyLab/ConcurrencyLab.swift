public actor ScoreBoard: Sendable {
    private var scores: [String: Int] = [:]
    public init() {}

    public func setScore(_ score: Int, for player: String) { scores[player] = score }
    public func score(for player: String) -> Int? { scores[player] }

    public func addPoints(_ points: Int, to player: String) {
        scores[player, default: 0] += points
    }
}

public enum AsyncExercises {
    public static func fakeFetch(id: String) async -> (id: String, value: Int) {
        try? await Task.sleep(for: .milliseconds(10))
        return (id, id.count)
    }

    public static func loadAll(ids: [String]) async -> [(id: String, value: Int)] {
        await withTaskGroup(of: (id: String, value: Int).self) { group in
            for id in ids {
                group.addTask { await fakeFetch(id: id) }
            }
            var results: [(id: String, value: Int)] = []
            for await item in group { results.append(item) }
            return results.sorted { $0.id < $1.id }
        }
    }
}
