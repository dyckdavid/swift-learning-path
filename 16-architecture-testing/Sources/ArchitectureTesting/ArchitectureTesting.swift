import Foundation

public struct TodoItem: Identifiable, Equatable, Sendable {
    public let id: UUID
    public var title: String
    public var isDone: Bool
    public init(id: UUID = UUID(), title: String, isDone: Bool = false) {
        self.id = id; self.title = title; self.isDone = isDone
    }
}

public protocol TodoRepository: Sendable {
    func all() async -> [TodoItem]
    func save(_ item: TodoItem) async
}

public actor InMemoryTodoRepository: TodoRepository {
    private var items: [TodoItem] = []
    public init() {}
    public func all() async -> [TodoItem] { items }
    public func save(_ item: TodoItem) async {
        if let idx = items.firstIndex(where: { $0.id == item.id }) { items[idx] = item }
        else { items.append(item) }
    }
}

public final class TodoViewModel: @unchecked Sendable {
    private let repository: any TodoRepository
    public private(set) var items: [TodoItem] = []

    public init(repository: any TodoRepository) {
        self.repository = repository
    }

// MARK: - TODO: MVVM + Swift Testing
/*
 Goal:
 Load/add/toggle todos through the view model; test behavior without UI.

 Steps:
 1. Implement `refresh()`, `add(title:)`, `toggle(id:)`.
 2. Keep transformation logic in the view model / repository — not in SwiftUI views.
 3. Write `#expect` / `#require` tests in the test target.

 Hints:
 - Swift Testing ships with the toolchain — `import Testing`.
 - https://developer.apple.com/documentation/testing

 Acceptance criteria:
 - Tests cover add + toggle without flaking.

 Docs:
 - https://developer.apple.com/documentation/testing
 - https://docs.swift.org/latest/documentation/testing/expectations/
 - https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app
*/

    // public func refresh() async { fatalError("TODO") }
    // public func add(title: String) async { fatalError("TODO") }
    // public func toggle(id: UUID) async { fatalError("TODO") }
}
