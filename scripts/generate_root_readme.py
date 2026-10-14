#!/usr/bin/env python3
"""Write top-level README, progress checklist, and .gitignore."""

from pathlib import Path

ROOT = Path("/workspace")

README = r'''# Swift Learning Path

A hands-on course for **David**: open each project in Xcode (or SwiftPM), complete the commented TODO assignments, and progress from Swift language fundamentals to pro-level iOS/macOS shipping skills — including CloudKit, StoreKit, accessibility, macros, CI/TestFlight, and iOS/macOS **27**-era APIs (Liquid Glass, WWDC26 SwiftUI, Foundation Models).

This repository is **scaffolding only** on `main` (starter code compiles; solutions are commented TODO blocks). Full worked solutions live on the **`solutions`** branch.

## Required tooling

| Tool | Recommendation |
|------|----------------|
| **Xcode** | **Xcode 27** (iOS / macOS / watchOS 27 SDKs) for projects 06–31 |
| **Swift** | Swift 6 language mode (Swift 6.0+ toolchain) |
| **Apple Developer Program** | Needed for CloudKit, Push, TestFlight, real device capabilities |
| **Apple Intelligence device** | Needed to exercise Foundation Models on-device (project 20) |

Projects **01–05**, **11**, **16–17**, and parts of **26** are Swift packages and can also be built with `swift build` / `swift test` on macOS or Linux. Everything that imports SwiftUI, SwiftData, CloudKit, WidgetKit, etc. requires a Mac + Xcode.

> **Cloud note:** This course was authored without Xcode in CI. Package projects are compile-tested on Linux where possible; Apple-framework projects are carefully scaffolded and flagged as **untested** in each README.

## How to use `main` vs `solutions`

1. Stay on **`main`** while learning — READMEs + TODO blocks only.
2. Open a project folder in Xcode (`*.xcodeproj` or `Package.swift`).
3. Implement TODOs until acceptance criteria pass.
4. When stuck, check the same path on **`solutions`** (spoiler branch) or diff against it.
5. Track progress in [PROGRESS.md](./PROGRESS.md).

```bash
git switch main          # assignments
git switch solutions     # completed reference implementations
```

## Roadmap

| # | Folder | Focus | Kind | Linux verify |
|---|--------|-------|------|--------------|
| 01 | [01-swift-basics](./01-swift-basics) | Types, optionals, collections | SwiftPM | `swift test` |
| 02 | [02-functions-closures](./02-functions-closures) | Functions, control flow, closures | SwiftPM | `swift test` |
| 03 | [03-types-and-oop](./03-types-and-oop) | Structs, classes, enums | SwiftPM | `swift test` |
| 04 | [04-protocols-generics-errors](./04-protocols-generics-errors) | Protocols, generics, errors | SwiftPM | `swift test` |
| 05 | [05-concurrency](./05-concurrency) | async/await, actors, Swift 6 | SwiftPM | `swift test` |
| 06 | [06-swiftui-basics](./06-swiftui-basics) | SwiftUI views & layout | Xcode iOS | Apple-only |
| 07 | [07-navigation-lists](./07-navigation-lists) | NavigationStack & List | Xcode iOS | Apple-only |
| 08 | [08-state-observation](./08-state-observation) | @Observable & state | Xcode iOS | Apple-only |
| 09 | [09-forms](./09-forms) | Forms & validation | Xcode iOS | Apple-only |
| 10 | [10-animations](./10-animations) | Animations & transitions | Xcode iOS | Apple-only |
| 11 | [11-networking-codable](./11-networking-codable) | URLSession + Codable | SwiftPM | `swift test` |
| 12 | [12-swiftdata](./12-swiftdata) | SwiftData local | Xcode iOS | Apple-only |
| 13 | [13-cloudkit-fundamentals](./13-cloudkit-fundamentals) | CloudKit private/public DB | Xcode iOS | Apple-only |
| 14 | [14-swiftdata-cloudkit](./14-swiftdata-cloudkit) | SwiftData + CloudKit sync | Xcode iOS | Apple-only |
| 15 | [15-cloudkit-sharing](./15-cloudkit-sharing) | CKShare / shared DB | Xcode iOS | Apple-only |
| 16 | [16-architecture-testing](./16-architecture-testing) | MVVM + Swift Testing | SwiftPM | `swift test` |
| 17 | [17-modularization](./17-modularization) | Modular Swift packages | SwiftPM | `swift build` |
| 18 | [18-widgets-live-activities](./18-widgets-live-activities) | WidgetKit + ActivityKit | Xcode iOS (+ extension) | Apple-only |
| 19 | [19-app-intents](./19-app-intents) | App Intents / Siri / Shortcuts | Xcode iOS | Apple-only |
| 20 | [20-foundation-models](./20-foundation-models) | Apple Intelligence / Foundation Models | Xcode iOS | Apple-only |
| 21 | [21-accessibility](./21-accessibility) | VoiceOver & Dynamic Type | Xcode iOS | Apple-only |
| 22 | [22-localization](./22-localization) | String Catalogs | Xcode iOS | Apple-only |
| 23 | [23-storekit](./23-storekit) | StoreKit 2 IAP | Xcode iOS | Apple-only |
| 24 | [24-push-notifications](./24-push-notifications) | UserNotifications + APNs | Xcode iOS | Apple-only |
| 25 | [25-performance](./25-performance) | Instruments & hitches | Xcode iOS | Apple-only |
| 26 | [26-swift-macros](./26-swift-macros) | Macro authoring package | SwiftPM | network + toolchain |
| 27 | [27-macos-app](./27-macos-app) | macOS SwiftUI app | Xcode Mac | Apple-only |
| 28 | [28-watchos-companion](./28-watchos-companion) | watchOS companion | Xcode (+ Watch target) | Apple-only |
| 29 | [29-liquid-glass-ios27](./29-liquid-glass-ios27) | Liquid Glass + iOS 27 APIs | Xcode iOS | Apple-only |
| 30 | [30-ci-release](./30-ci-release) | Xcode Cloud / fastlane / TestFlight | Docs + templates | N/A |
| 31 | [31-capstone](./31-capstone) | Capstone — StudyPilot | Xcode iOS | Apple-only |

## Suggested pacing

1. **Language core (01–05)** — finish with confidence in Swift 6 concurrency.
2. **SwiftUI vertical slice (06–12)** — UI → networking → persistence.
3. **Cloud sync & sharing (13–15)** — know the SwiftData+CloudKit vs CKShare boundary.
4. **Architecture (16–17)** — testable modules before more frameworks.
5. **System integrations (18–24)** — widgets, intents, AI, a11y, l10n, IAP, push.
6. **Pro polish (25–30)** — performance, macros, multiplatform, release engineering.
7. **Capstone (31)** — ship something coherent.

## Important API notes (researched)

- **Liquid Glass** — adopt via standard SwiftUI/UIKit components and `glassEffect` APIs; see [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass).
- **WWDC26 / iOS 27 SwiftUI** — resizable iPhone apps, toolbar overflow/visibility APIs, document APIs, AsyncImage caching; see [What’s new in SwiftUI](https://developer.apple.com/videos/play/wwdc2026/269/).
- **Foundation Models** — `LanguageModelSession`, `@Generable`, tools; see [Foundation Models](https://developer.apple.com/documentation/foundationmodels).
- **SwiftData + CloudKit sharing** — private sync is supported via `ModelConfiguration.CloudKitDatabase`; **CKShare-style collaborative sharing is not native to SwiftData as of WWDC26** (Apple DTS). Use project **15** (CloudKit/Core Data sharing) for that path.
- Where an API could not be fully signature-verified in this environment, the project README says so explicitly — **do not invent APIs**; confirm in Xcode’s DocC for your SDK.

## Regenerating Xcode projects

App projects include a committed `*.xcodeproj/project.pbxproj` and a `project.yml` (XcodeGen). On a Mac, if a project fails to open cleanly:

```bash
brew install xcodegen
cd <project>
xcodegen generate
```

## License

Learning materials for personal use. Third-party services (JSONPlaceholder, etc.) have their own terms.
'''

PROGRESS = '''# Progress checklist

Mark items as you complete them on `main` (implement TODOs + acceptance criteria). Peek at `solutions` only when needed.

## Language fundamentals
- [ ] 01 Swift basics
- [ ] 02 Functions & closures
- [ ] 03 Structs, classes, enums
- [ ] 04 Protocols, generics, errors
- [ ] 05 Concurrency (Swift 6)

## SwiftUI & data
- [ ] 06 SwiftUI basics
- [ ] 07 Navigation & lists
- [ ] 08 State & Observation
- [ ] 09 Forms
- [ ] 10 Animations
- [ ] 11 Networking + Codable
- [ ] 12 SwiftData (local)

## CloudKit
- [ ] 13 CloudKit fundamentals (private/public)
- [ ] 14 SwiftData + CloudKit sync
- [ ] 15 CloudKit sharing (CKShare)

## Architecture
- [ ] 16 MVVM + Swift Testing
- [ ] 17 Modularization with packages

## System features
- [ ] 18 Widgets & Live Activities
- [ ] 19 App Intents / Siri / Shortcuts
- [ ] 20 Foundation Models (Apple Intelligence)
- [ ] 21 Accessibility
- [ ] 22 Localization (String Catalogs)
- [ ] 23 StoreKit 2
- [ ] 24 Push notifications

## Pro-level
- [ ] 25 Performance & Instruments
- [ ] 26 Swift macros package
- [ ] 27 macOS app
- [ ] 28 watchOS companion
- [ ] 29 Liquid Glass & iOS 27 APIs
- [ ] 30 CI / TestFlight / App Store release
- [ ] 31 Capstone — StudyPilot
'''

GITIGNORE = '''\
.DS_Store
/.build
/**/.build
/Packages
/**/*.xcodeproj/xcuserdata
/**/*.xcworkspace/xcuserdata
/**/DerivedData
/**/.swiftpm
**/xcuserdata/
*.xcuserstate
.swiftpm
Package.resolved
**/Package.resolved
.idea
'''


def main() -> None:
    (ROOT / "README.md").write_text(README, encoding="utf-8")
    (ROOT / "PROGRESS.md").write_text(PROGRESS, encoding="utf-8")
    (ROOT / ".gitignore").write_text(GITIGNORE, encoding="utf-8")
    print("Root README + PROGRESS + gitignore written")


if __name__ == "__main__":
    main()
