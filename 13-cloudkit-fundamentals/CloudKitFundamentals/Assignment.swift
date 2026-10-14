import CloudKit

enum CloudKitPlayground {
    /// Replace with your container ID after enabling iCloud in Signing & Capabilities.
    static let containerID = "iCloud.com.swiftlearning.REPLACE_ME"

    static var container: CKContainer { CKContainer(identifier: containerID) }
    static var privateDB: CKDatabase { container.privateCloudDatabase }
    static var publicDB: CKDatabase { container.publicCloudDatabase }
}
// MARK: - TODO: Private vs public database write/read
/*
 Goal:
 Save a CKRecord to the private DB and fetch it back; understand public DB use cases.

 Steps:
 1. Create a CKRecord(recordType: "Idea") with a "text" string field.
 2. `try await privateDB.save(record)`.
 3. Fetch with `record(for:)` using the saved recordID.
 4. Write a short comment in code: when would you use publicCloudDatabase instead?

 Hints:
 - You need a real Apple Developer team + iCloud capability for device/simulator signed-in iCloud.
 - Simulator iCloud sign-in is required.
 - Start in Development environment in CloudKit Console.

 Acceptance criteria:
 - Save/fetch succeeds when container + iCloud account are configured.

 Docs:
 - https://developer.apple.com/documentation/cloudkit
 - https://developer.apple.com/documentation/cloudkit/ckcontainer
 - https://developer.apple.com/documentation/cloudkit/ckdatabase
 - https://developer.apple.com/documentation/cloudkit/ckrecord
*/
