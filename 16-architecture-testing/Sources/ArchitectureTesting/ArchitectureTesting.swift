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

    public func refresh() async {
        items = await repository.all()
    }

    public func add(title: String) async {
        let item = TodoItem(title: title)
        await repository.save(item)
        await refresh()
    }

    public func toggle(id: UUID) async {
        guard var item = items.first(where: { $0.id == id }) else { return }
        item.isDone.toggle()
        await repository.save(item)
        await refresh()
    }
}
