import SwiftData

// MARK: - TODO model
// @Model
// final class Note {
//     var title: String
//     var createdAt: Date
//     init(title: String, createdAt: Date = .now) {
//         self.title = title
//         self.createdAt = createdAt
//     }
// }
// MARK: - TODO: SwiftData CRUD list
/*
 Goal:
 Persist notes with SwiftData and show them in a List.

 Steps:
 1. Uncomment the Note @Model.
 2. Attach `.modelContainer(for: Note.self)` to the App (or WindowGroup content).
 3. Use @Query to list notes; toolbar button inserts a note; swipe deletes.

 Hints:
 - Start with an in-memory configuration for Previews.
 - https://developer.apple.com/documentation/swiftdata/modelcontainer

 Acceptance criteria:
 - Notes persist across launches on device/simulator (disk config).

 Docs:
 - https://developer.apple.com/documentation/swiftdata
 - https://developer.apple.com/documentation/swiftdata/model()
 - https://developer.apple.com/documentation/swiftdata/query
*/
