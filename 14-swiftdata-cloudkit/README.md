# 14. SwiftData + CloudKit Sync

## Concepts
- ModelConfiguration.CloudKitDatabase
- Private sync
- Multi-device testing
- Limitations vs sharing

## What you’ll build
Synced task list via SwiftData’s CloudKit private database integration.

## Project type
Xcode iOS app

## Steps overview
1. Enable CloudKit
2. Configure ModelContainer
3. Verify multi-device sync

## Stretch goals
- Handle sync conflicts / dense updates thoughtfully

## Required tooling
Xcode 27 + iCloud capability + Developer account.

## Docs (verify APIs here)
- [ModelConfiguration](https://developer.apple.com/documentation/swiftdata/modelconfiguration)
- [CloudKitDatabase](https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase)

## Untested / Apple-only notes
- Apple-only; not verified in this Linux environment.
- **API uncertainty / limitation:** SwiftData+CloudKit does not natively support CKShare-style collaborative sharing as of WWDC26 (use project 15 for sharing).
- See: https://developer.apple.com/forums/thread/829707

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
