import CloudKit
import SwiftUI

/// Sharing requires CloudKit (CKShare) or Core Data + NSPersistentCloudKitContainer.
/// SwiftData does not natively support CKShare as of WWDC26 — see README.
// MARK: - TODO: Create and present a CKShare
/*
 Goal:
 Share a root CKRecord with another iCloud user via share URL / share UI.

 Steps:
 1. Ensure shareable records live in a **custom zone** in the private database.
 2. Create `CKShare(rootRecord:)` (hierarchy) or `CKShare(recordZoneID:)` (zone share).
 3. Save share + root together with `modifyRecords(saving:deleting:)`.
 4. Present sharing UI (e.g. `UICloudSharingController` / `CloudSharingView` where available) or distribute `share.url`.
 5. Accept share on a second account and read from `sharedCloudDatabase`.

 Hints:
 - Follow Apple’s CloudKit sharing guidance carefully — this is the hardest CloudKit topic.
 - Core Data path: `NSPersistentCloudKitContainer` sharing sample from Apple is a valid alternative.

 Acceptance criteria:
 - Second iCloud account can see shared records in sharedCloudDatabase.

 Docs:
 - https://developer.apple.com/documentation/cloudkit/ckshare
 - https://developer.apple.com/documentation/cloudkit/sharedcloudkitcontainer
 - https://developer.apple.com/videos/play/tech-talks/10874/
 - https://developer.apple.com/documentation/coredata/sharing_core_data_objects_between_icloud_users
*/
