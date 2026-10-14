import Foundation

public struct TodoDTO: Equatable, Sendable, Identifiable {
    public let id: UUID
    public var title: String
    public init(id: UUID = UUID(), title: String) {
        self.id = id
        self.title = title
    }
}

public enum CoreVersion {
    public static let string = "1.0.0"
}
