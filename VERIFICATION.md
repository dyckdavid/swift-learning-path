# Compile verification log

Environment: Linux + Swift 6.4.1 (swiftly). No Xcode / Apple SDKs available.

## Verified with `swift test` (pass)

- 01-swift-basics
- 02-functions-closures
- 03-types-and-oop
- 04-protocols-generics-errors
- 05-concurrency
- 11-networking-codable (uses `FoundationNetworking` on Linux)
- 16-architecture-testing
- 17-modularization

## Verified with `swift test` (also)

- 26-swift-macros — starter `ExpressionMacro` placeholder expansion builds/tests on Linux (full stringify on `solutions`).

## Not compile-verified here (Apple frameworks / Xcode)

06–10, 12–15, 18–25, 27–29, 31 (SwiftUI / SwiftData / CloudKit / WidgetKit / ActivityKit / AppIntents / FoundationModels / StoreKit / UserNotifications / macOS / watchOS).

30 is documentation + CI templates only.

## API uncertainties explicitly flagged in project READMEs

- WWDC26 toolbar helpers (`visibilityPriority`, `ToolbarOverflowMenu`, `topBarPinnedTrailing`) — from session transcripts; confirm in your SDK DocC.
- Foundation Models initializer overload details — confirm in installed SDK.
- SwiftData has **no native CKShare** as of WWDC26 (Apple DTS) — covered in projects 14–15.
- StoreKit Configuration JSON may be rewritten by Xcode on first open.
- Generated `.xcodeproj` files were authored without Xcode; regenerate via `xcodegen` from `project.yml` if needed.
