import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\.modelContext) private var context
    @Query private var tasks: [SyncedTask]

    var body: some View {
        NavigationStack {
            List {
                ForEach(tasks) { task in
                    Toggle(task.title, isOn: Binding(
                        get: { task.isDone },
                        set: { task.isDone = $0 }
                    ))
                }
            }
            .navigationTitle("Tasks")
            .toolbar {
                Button("Add") {
                    context.insert(SyncedTask(title: "Task \(tasks.count + 1)"))
                }
            }
        }
    }
}
