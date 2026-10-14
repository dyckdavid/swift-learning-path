import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var context
    @Query(sort: \Note.createdAt, order: .reverse) private var notes: [Note]
    var body: some View {
        NavigationStack {
            List {
                ForEach(notes) { note in
                    Text(note.title)
                }
                .onDelete { indexSet in
                    for index in indexSet { context.delete(notes[index]) }
                }
            }
            .navigationTitle("Notes")
            .toolbar {
                Button("Add") {
                    context.insert(Note(title: "Note \(notes.count + 1)"))
                }
            }
        }
    }
}
