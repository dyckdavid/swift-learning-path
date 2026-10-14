# 13. CloudKit Fundamentals

## Concepts
- CKContainer
- privateCloudDatabase vs publicCloudDatabase
- CKRecord save/fetch
- iCloud capability

## What you’ll build
A minimal Idea record writer/reader using CloudKit directly.

## Project type
Xcode iOS app + CloudKit entitlements

## Steps overview
1. Enable iCloud/CloudKit capability with your team
2. Replace container ID
3. Implement save/fetch TODO

## Stretch goals
- Query records with CKQuery
- Observe CKAccountStatus

## Required tooling
Xcode 27 + paid Apple Developer account for CloudKit; iCloud-signed simulator/device.

## Docs (verify APIs here)
- [CloudKit](https://developer.apple.com/documentation/cloudkit)
- [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase)

## Untested / Apple-only notes
- Cannot be compile-verified here (no Xcode / no Apple cloud credentials).
- Entitlements use a placeholder container ID — replace before running.
- Public DB writes require careful security roles in CloudKit Dashboard.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
