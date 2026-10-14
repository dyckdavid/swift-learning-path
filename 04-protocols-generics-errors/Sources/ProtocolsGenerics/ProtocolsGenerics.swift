import Foundation

public protocol IdentifiableItem: Sendable {
    var id: String { get }
}

public struct User: IdentifiableItem, Equatable, Sendable {
    public let id: String
    public var name: String
    public init(id: String, name: String) { self.id = id; self.name = name }
}

public enum StoreError: Error, Equatable, Sendable {
    case notFound(id: String)
    case emptyName
}

public struct MemoryStore<Item: IdentifiableItem>: Sendable {
    private var items: [String: Item]
    public init(items: [Item] = []) {
        self.items = Dictionary(uniqueKeysWithValues: items.map { ($0.id, $0) })
    }

    public func all() -> [Item] { Array(items.values) }

    public func item(id: String) throws -> Item {
        guard let item = items[id] else { throw StoreError.notFound(id: id) }
        return item
    }

    public mutating func upsert(_ item: Item) {
        items[item.id] = item
    }
}

public func validatedName(_ raw: String) throws -> String {
    let trimmed = raw.trimmingCharacters(in: .whitespacesAndNewlines)
    guard !trimmed.isEmpty else { throw StoreError.emptyName }
    return trimmed
}
