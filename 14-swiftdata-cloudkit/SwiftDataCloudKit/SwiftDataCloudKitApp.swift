import SwiftUI
import SwiftData

@main
struct SwiftDataCloudKitApp: App {
    private let container: ModelContainer = {
        let config = ModelConfiguration(cloudKitDatabase: .automatic)
        return try! ModelContainer(for: SyncedTask.self, configurations: config)
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(container)
    }
}
