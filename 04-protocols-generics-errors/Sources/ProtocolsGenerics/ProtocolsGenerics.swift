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

// MARK: - TODO: Generics + throwing APIs
/*
 Goal:
 Complete store operations with typed errors.

 Steps:
 1. Implement `item(id:)` throwing `StoreError.notFound`.
 2. Implement `upsert` mutating method.
 3. Implement free function `validatedName(_:)` that throws `emptyName` for blank strings.

 Hints:
 - Use `guard let` + `throw`.
 - Trim whitespace before validating names.

 Acceptance criteria:
 - Missing id throws `.notFound`
 - "   " throws `.emptyName`

 Docs:
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/
 - https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/
*/

    // public func item(id: String) throws -> Item { fatalError("TODO") }
    // public mutating func upsert(_ item: Item) { fatalError("TODO") }
}

// public func validatedName(_ raw: String) throws -> String { fatalError("TODO") }
