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
// MARK: - TODO: List + NavigationStack detail
/*
 Goal:
 Show SampleData.items in a List and push a detail screen.

 Steps:
 1. Use NavigationStack + List(SampleData.items).
 2. Each row is a NavigationLink to a detail view showing the title.
 3. Support swipe-to-delete OR a toolbar EditButton (your choice).

 Hints:
 - Prefer value-based NavigationLink(value:) + navigationDestination(for:).
 - WWDC26 adds richer reorder APIs — optional stretch; see docs.

 Acceptance criteria:
 - Tapping a row shows detail; back navigation works.

 Docs:
 - https://developer.apple.com/documentation/swiftui/navigationstack
 - https://developer.apple.com/documentation/swiftui/list
 - https://developer.apple.com/videos/play/wwdc2026/269/
*/
