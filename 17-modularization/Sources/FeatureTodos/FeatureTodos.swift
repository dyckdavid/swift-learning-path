import Core

public enum TodoFeature {
    public static func sample() -> [TodoDTO] {
        [TodoDTO(title: "Learn modules")]
    }

    public static func openTodos(in items: [TodoDTO]) -> [TodoDTO] {
        items.filter { !$0.title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty }
    }
}
