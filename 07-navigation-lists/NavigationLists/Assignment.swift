import SwiftUI

struct SampleItem: Identifiable, Hashable {
    let id: UUID
    var title: String
    init(title: String) { self.id = UUID(); self.title = title }
}

enum SampleData {
    static let items: [SampleItem] = [
        .init(title: "NavigationStack"),
        .init(title: "List"),
        .init(title: "NavigationLink"),
    ]
}

struct LibraryRoot: View {
    @State private var items = SampleData.items
    var body: some View {
        List {
            ForEach(items) { item in
                NavigationLink(value: item) { Text(item.title) }
            }
            .onDelete { items.remove(atOffsets: $0) }
        }
        .navigationDestination(for: SampleItem.self) { item in
            Text(item.title).font(.largeTitle)
        }
        .toolbar { EditButton() }
    }
}
