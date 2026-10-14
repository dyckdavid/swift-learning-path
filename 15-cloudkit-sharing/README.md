# 15. CloudKit Sharing (CKShare)

## Concepts
- CKShare
- sharedCloudDatabase
- Custom zones
- Optional Core Data sharing stack

## What you’ll build
Invite another user to a shared record hierarchy or zone.

## Project type
Xcode iOS app

## Steps overview
1. Implement share creation
2. Test with two Apple IDs
3. Read accepted shares from shared DB

## Stretch goals
- Zone-wide share vs root-record hierarchy
- Participant permissions

## Required tooling
Xcode 27 + two iCloud accounts + Developer account.

## Docs (verify APIs here)
- [CKShare](https://developer.apple.com/documentation/cloudkit/ckshare)
- [Get the most out of CloudKit Sharing](https://developer.apple.com/videos/play/tech-talks/10874/)

## Untested / Apple-only notes
- Not verified in CI/Linux.
- **Verified limitation:** SwiftData+CloudKit has no native CKShare support as of WWDC26; this project uses CloudKit (or Core Data) APIs instead.
- UICloudSharingController is UIKit; SwiftUI `CloudSharingView` availability varies by OS — check docs for your SDK and fall back if needed.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
