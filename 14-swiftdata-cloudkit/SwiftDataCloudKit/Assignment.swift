import SwiftData

// @Model
// final class SyncedTask {
//     var title: String
//     var isDone: Bool
//     init(title: String, isDone: Bool = false) {
//         self.title = title
//         self.isDone = isDone
//     }
// }
// MARK: - TODO: SwiftData ↔ CloudKit private sync
/*
 Goal:
 Mirror tasks across devices using SwiftData’s CloudKit integration (private database).

 Steps:
 1. Uncomment SyncedTask @Model.
 2. Create ModelConfiguration(cloudKitDatabase: .automatic) or .private("iCloud.com…").
 3. Build ModelContainer(for: SyncedTask.self, configurations: config).
 4. Run on two signed-in devices/simulators and confirm sync.

 Hints:
 - SwiftData+CloudKit syncs the **private** database; it does **not** natively support CKShare user-to-user sharing (confirmed by Apple DTS / forums as of WWDC26).
 - Bundle ID + container must match entitlements.

 Acceptance criteria:
 - Records created on device A appear on device B when both use same iCloud account.

 Docs:
 - https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:)
 - https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase
 - https://developer.apple.com/documentation/swiftdata
*/
