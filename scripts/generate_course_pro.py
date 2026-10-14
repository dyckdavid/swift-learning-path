#!/usr/bin/env python3
"""Generate pro-level projects 17–31."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_course import (  # noqa: E402
    ROOT,
    app_sources,
    generate_xcode_app,
    package_swift,
    readme_project,
    todo_block,
    write,
)
from generate_course_apps import CLOUDKIT_ENTITLEMENTS, PUSH_ENTITLEMENTS  # noqa: E402


def project_17():
    d = ROOT / "17-modularization"
    # Workspace-style multi-package
    write(d / "README.md", readme_project(
        "17", "App Architecture at Scale — Modular Packages",
        ["Swift Package modularization", "Feature modules vs core", "Dependency direction", "Local package product linking"],
        "A small modular workspace: `Core`, `FeatureTodos`, and `AppShell` executable that depends on features.",
        [
            "Explore the three packages under this folder",
            "Keep Feature → Core dependencies only (no Feature ↔ Feature cycles)",
            "Implement the TODO in FeatureTodos that uses Core models",
            "Build with `swift build` from AppShell",
        ],
        ["Add a FeatureSettings package", "Introduce a public protocol in Core for analytics"],
        "Xcode 16+ / Swift 6; Linux `swift build` OK for packages.",
        ["iOS UI shell is package-based here; shipping App Store apps still need an Xcode app target that links local packages."],
        "Multi-package SwiftPM workspace",
        [("Organizing your code with Swift packages", "https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages"),
         ("SwiftPM", "https://docs.swift.org/package-manager/")],
    ))
    write(d / "Package.swift", '''\
// swift-tools-version: 6.0
import PackageDescription

// Root umbrella package so `swift build` works from 17-modularization/
let package = Package(
    name: "ModularWorkspace",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "Core", targets: ["Core"]),
        .library(name: "FeatureTodos", targets: ["FeatureTodos"]),
        .executable(name: "AppShell", targets: ["AppShell"]),
    ],
    targets: [
        .target(name: "Core"),
        .target(name: "FeatureTodos", dependencies: ["Core"]),
        .executableTarget(name: "AppShell", dependencies: ["FeatureTodos", "Core"]),
        .testTarget(name: "CoreTests", dependencies: ["Core"]),
    ]
)
''')
    write(d / "Sources" / "Core" / "Core.swift", '''\
import Foundation

public struct TodoDTO: Equatable, Sendable, Identifiable {
    public let id: UUID
    public var title: String
    public init(id: UUID = UUID(), title: String) {
        self.id = id
        self.title = title
    }
}

public enum CoreVersion {
    public static let string = "1.0.0"
}
''')
    write(d / "Sources" / "FeatureTodos" / "FeatureTodos.swift", f'''\
import Core

public enum TodoFeature {{
    public static func sample() -> [TodoDTO] {{
        [TodoDTO(title: "Learn modules")]
    }}

{todo_block(
    "Feature API on top of Core",
    "Add a filter helper that belongs in the feature module but uses Core DTOs.",
    ["Implement `openTodos(in:)` returning items whose titles are non-empty.",
     "Do not invent networking here — keep the feature pure."],
    ["Depend only on Core."],
    ["Filters out empty titles."],
    ["https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages"],
)}
    // public static func openTodos(in items: [TodoDTO]) -> [TodoDTO] {{ fatalError("TODO") }}
}}
''')
    write(d / "Sources" / "AppShell" / "main.swift", '''\
import Core
import FeatureTodos

print("AppShell", CoreVersion.string, "samples:", TodoFeature.sample().count)
''')
    write(d / "Tests" / "CoreTests" / "CoreTests.swift", '''\
import Testing
import Core

@Test func dtoIdentity() {
    let a = TodoDTO(title: "A")
    #expect(a.title == "A")
}
''')


def project_18():
    name = "WidgetsLiveActivities"
    d = ROOT / "18-widgets-live-activities"
    # Main app + notes for widget extension (extension target hard to fake perfectly — document Xcode steps)
    extra = '''
import ActivityKit

/// Live Activity attributes scaffold (ActivityKit).
/// NOTE: Widget extension target must be added in Xcode (File → New → Target → Widget Extension).
/// This app target only holds shared attributes + start/stop helpers.

struct FocusAttributes: ActivityAttributes {
    public struct ContentState: Codable, Hashable, Sendable {
        var secondsRemaining: Int
        var phaseName: String
    }

    var taskName: String
}
''' + todo_block(
        "Widget timeline + Live Activity",
        "Ship a home-screen widget and a Live Activity for a focus timer.",
        [
            "In Xcode: add a Widget Extension; enable Live Activities in Info.plist (`NSSupportsLiveActivities`).",
            "Implement a `TimelineProvider` + `View` for `.systemSmall` (and optionally `.systemExtraLargePortrait` on iOS 27).",
            "Implement `ActivityConfiguration` for `FocusAttributes` (Lock Screen + Dynamic Island).",
            "From the app, `Activity.request` / `update` / `end` using ActivityKit.",
        ],
        [
            "WWDC26: Live Activities essentials — https://developer.apple.com/videos/play/wwdc2026/223/",
            "WWDC26: WidgetKit foundations — https://developer.apple.com/videos/play/wwdc2026/277/",
        ],
        ["Widget renders glanceable state; Live Activity updates while timer runs."],
        [
            "https://developer.apple.com/documentation/widgetkit",
            "https://developer.apple.com/documentation/activitykit",
            "https://developer.apple.com/documentation/activitykit/activity",
            "https://developer.apple.com/videos/play/wwdc2026/223/",
            "https://developer.apple.com/videos/play/wwdc2026/277/",
        ],
    )
    sources = app_sources(name, "Widgets & Live Activities", "WidgetKit + ActivityKit", "Focus", "\n" + extra)
    # ActivityAttributes needs import — may fail without ActivityKit on non-Apple; it's in app sources for Xcode
    generate_xcode_app(d, name, "com.swiftlearning.WidgetsLiveActivities", sources, deployment="17.0")
    write(d / "WidgetExtension" / "README.md", '''\
# Widget Extension (create in Xcode)

This folder is a placeholder. On your Mac:

1. Open `WidgetsLiveActivities.xcodeproj`
2. File → New → Target → **Widget Extension**
3. Enable **Include Live Activity** if the template offers it
4. Move shared `FocusAttributes` into a shared framework or shared folder membership (app + extension)

Info.plist keys to confirm:
- `NSSupportsLiveActivities` = YES (app)
- Relevant App Group if sharing data with UserDefaults/files
''')
    write(d / "README.md", readme_project(
        "18", "Widgets & Live Activities",
        ["WidgetKit timelines", "ActivityKit", "Dynamic Island presentations", "App Groups (optional)"],
        "Focus timer widget + Live Activity.",
        ["Add Widget Extension target in Xcode", "Implement timeline + ActivityConfiguration", "Start/update/end from app"],
        ["ActivityKit push updates", "Interactive widget buttons"],
        "Xcode 27 / iOS 17+ (Live Activities); physical device recommended for Dynamic Island.",
        [
            "Extension target cannot be fully authored without Xcode — placeholder documented.",
            "ActivityKit/WidgetKit Apple-only; not buildable on Linux.",
            "iOS 27 landscape Dynamic Island style covered in WWDC26 session 223 — adopt when available in your SDK.",
        ],
        "Xcode iOS app + (you add) Widget Extension",
        [("WidgetKit", "https://developer.apple.com/documentation/widgetkit"),
         ("ActivityKit", "https://developer.apple.com/documentation/activitykit"),
         ("Live Activities essentials — WWDC26", "https://developer.apple.com/videos/play/wwdc2026/223/")],
    ))


def project_19():
    name = "AppIntentsLab"
    d = ROOT / "19-app-intents"
    extra = '''
import AppIntents

// MARK: - Starter intent (compiles); expand via TODOs
struct OpenStudyIntent: AppIntent {
    static var title: LocalizedStringResource = "Open Study Session"
    static var description = IntentDescription("Opens the study session screen.")

    func perform() async throws -> some IntentResult {
        // TODO: route into your app (dependencies / app enum navigation)
        return .result()
    }
}
''' + todo_block(
        "App Intent + App Shortcut",
        "Expose a parameterised intent to Shortcuts / Siri / Spotlight.",
        [
            "Add an `@Parameter` (e.g. minutes: Int) to an intent.",
            "Return a dialog or opensIntent result as appropriate.",
            "Implement `AppShortcutsProvider` with phrases using `\\(.applicationName)`.",
            "Run from Shortcuts app and via Siri phrase.",
        ],
        ["Keep intents focused on core user actions.",
         "https://developer.apple.com/documentation/appintents/appintent"],
        ["Intent appears in Shortcuts; App Shortcut phrase invokes it."],
        [
            "https://developer.apple.com/documentation/appintents",
            "https://developer.apple.com/documentation/appintents/appintent",
            "https://developer.apple.com/documentation/appintents/appshortcutsprovider",
            "https://developer.apple.com/videos/play/wwdc2025/244/",
        ],
    )
    sources = app_sources(name, "App Intents", "Siri & Shortcuts", "Intents", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.AppIntentsLab", sources)
    write(d / "README.md", readme_project(
        "19", "App Intents, Siri & Shortcuts",
        ["AppIntent", "@Parameter", "AppShortcutsProvider", "Discovery via Spotlight/Siri"],
        "A study-session intent with an App Shortcut phrase.",
        ["Extend OpenStudyIntent", "Add AppShortcutsProvider", "Test in Shortcuts + Siri"],
        ["App Entities for selectable study topics"],
        "Xcode 27 recommended; device with Siri for voice.",
        ["Apple-only; not verified on Linux.", "Siri AI / iOS 27 conversational features may add new surfaces — stick to App Intents APIs documented for your SDK."],
        "Xcode iOS app",
        [("App Intents", "https://developer.apple.com/documentation/appintents"),
         ("Get to know App Intents — WWDC25", "https://developer.apple.com/videos/play/wwdc2025/244/")],
    ))


def project_20():
    name = "FoundationModelsLab"
    d = ROOT / "20-foundation-models"
    # Avoid importing FoundationModels in starter so older toolchains don't break the pbx;
    # keep API references in comments + TODO with verified names from docs.
    extra = todo_block(
        "On-device language model session",
        "Use the Foundation Models framework to summarize text on-device.",
        [
            "`import FoundationModels`",
            "Create a `LanguageModelSession` (optionally with instructions / tools).",
            "Call `respond` (or streaming `streamResponse`) with a user prompt.",
            "Define a `@Generable` struct (e.g. title + bullet points) and request typed output.",
            "Gate on Apple Intelligence availability / supported devices.",
        ],
        [
            "Framework docs: https://developer.apple.com/documentation/foundationmodels",
            "WWDC25 intro: https://developer.apple.com/videos/play/wwdc2025/286/",
            "WWDC25 deep dive: https://developer.apple.com/videos/play/wwdc2025/301/",
            "Newer SDKs also discuss Private Cloud Compute models and `LanguageModel` providers — only use APIs listed in your installed SDK’s doc archive.",
        ],
        ["Given a long paragraph, app shows a structured summary without a custom server."],
        [
            "https://developer.apple.com/documentation/foundationmodels",
            "https://developer.apple.com/documentation/foundationmodels/languagemodelsession",
            "https://developer.apple.com/foundation-models-framework/",
            "https://developer.apple.com/videos/play/wwdc2025/286/",
        ],
    ) + '''
/*
 Verified API names from Apple documentation (use autocomplete in Xcode 27 to confirm signatures):
 - import FoundationModels
 - LanguageModelSession
 - SystemLanguageModel / PrivateCloudComputeLanguageModel (availability varies)
 - @Generable / @Guide
 - Tool protocol for tool calling
 - session.respond / streamResponse

 If an initializer or type is missing in your SDK, do NOT invent it — check the doc page for your SDK
 and note the discrepancy in a comment.
*/
'''
    sources = app_sources(name, "Foundation Models", "Apple Intelligence on-device", "Summarize", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.FoundationModelsLab", sources, deployment="26.0")
    write(d / "README.md", readme_project(
        "20", "Apple Intelligence — Foundation Models",
        ["LanguageModelSession", "@Generable guided generation", "Tool calling (optional)", "Availability / device support"],
        "On-device text summarizer with structured output.",
        ["Import FoundationModels", "Implement session + Generable summary", "Handle unsupported devices gracefully"],
        ["Add a Tool that fetches local notes", "Try streaming tokens into the UI"],
        "**Xcode 27** + Apple Intelligence–capable Mac/iPhone. Deployment target set to iOS 26+ in project (adjust if your SDK expects 27).",
        [
            "Cannot compile/verify Foundation Models on Linux.",
            "Exact initializer signatures evolve — confirm in Xcode’s SDK docs; cited types are from Apple’s Foundation Models documentation.",
            "Private Cloud Compute / third-party LanguageModel providers: use only if present in your SDK docs.",
        ],
        "Xcode iOS app",
        [("Foundation Models", "https://developer.apple.com/documentation/foundationmodels"),
         ("LanguageModelSession", "https://developer.apple.com/documentation/foundationmodels/languagemodelsession"),
         ("Meet the Foundation Models framework — WWDC25", "https://developer.apple.com/videos/play/wwdc2025/286/")],
    ))


def project_21():
    name = "AccessibilityLab"
    d = ROOT / "21-accessibility"
    extra = todo_block(
        "VoiceOver & Dynamic Type",
        "Make a custom control accessible and respect Dynamic Type.",
        [
            "Replace a tappable RoundedRectangle with a real Button (or add accessibility traits/actions).",
            "Add `.accessibilityLabel` / `.accessibilityHint` / `.accessibilityValue` as needed.",
            "Use scalable fonts (`.font(.body)` etc.) and test with larger content sizes.",
            "Verify with Accessibility Inspector / VoiceOver on device.",
        ],
        ["Prefer native controls — they inherit accessibility.",
         "Combine elements with `accessibilityElement(children: .combine)` when appropriate."],
        ["VoiceOver reads meaningful labels; UI remains usable at XXXL content size."],
        [
            "https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)",
            "https://developer.apple.com/documentation/accessibility",
            "https://developer.apple.com/accessibility/xcode/",
        ],
    )
    sources = app_sources(name, "Accessibility", "VoiceOver & Dynamic Type", "A11y", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.AccessibilityLab", sources)
    write(d / "README.md", readme_project(
        "21", "Accessibility",
        ["VoiceOver", "accessibility labels/hints/values", "Dynamic Type", "Accessibility Inspector"],
        "An intentionally imperfect UI you will repair for accessibility.",
        ["Audit with Inspector", "Fix labels and hit targets", "Retest with VoiceOver"],
        ["Reduce Motion alternative animations", "Smart invert / contrast checks"],
        "Xcode 27 + device/simulator with VoiceOver.",
        ["Linux untested."],
        "Xcode iOS app",
        [("Accessibility", "https://developer.apple.com/documentation/accessibility"),
         ("SwiftUI accessibilityLabel", "https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)")],
    ))


def project_22():
    name = "LocalizationLab"
    d = ROOT / "22-localization"
    extra = todo_block(
        "String Catalog localization",
        "Localize UI strings with a String Catalog and exercise plurals.",
        [
            "Enable `SWIFT_EMIT_LOC_STRINGS` (already on in project settings).",
            "Add `Localizable.xcstrings` (String Catalog) via Xcode.",
            "Replace hardcoded strings with `String(localized:)` / LocalizedStringResource / Text(\"key\").",
            "Add at least one plural variation (e.g. \"%lld tasks left\").",
            "Add a second language (e.g. Spanish) and switch device language to verify.",
        ],
        ["String Catalogs are the modern replacement for sprawling Localizable.strings workflows.",
         "https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog"],
        ["UI shows translated strings; plurals correct for 0/1/many."],
        [
            "https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog",
            "https://developer.apple.com/documentation/foundation/string/init(localized:)",
        ],
    )
    sources = app_sources(name, "Localization", "String Catalogs", "L10n", "\n" + extra)
    # Seed a minimal xcstrings JSON
    write(d / name / "Localizable.xcstrings", '''\
{
  "sourceLanguage" : "en",
  "strings" : {
    "Welcome" : {
      "extractionState" : "manual",
      "localizations" : {
        "en" : { "stringUnit" : { "state" : "translated", "value" : "Welcome" } },
        "es" : { "stringUnit" : { "state" : "translated", "value" : "Bienvenido" } }
      }
    }
  },
  "version" : "1.0"
}
''')
    generate_xcode_app(d, name, "com.swiftlearning.LocalizationLab", sources)
    write(d / "README.md", readme_project(
        "22", "Localization (String Catalogs)",
        ["String Catalog (.xcstrings)", "String(localized:)", "Plurals / variations", "Language switching"],
        "A welcome screen ready for English + Spanish (extend it).",
        ["Wire Text(LocalizedStringResource(\"Welcome\"))", "Add pluralized task count", "Test with scheme language overrides"],
        ["Localize accessibility labels too"],
        "Xcode 27 (String Catalog tools).",
        ["Full catalog workflow is Mac/Xcode-centric; not verified on Linux."],
        "Xcode iOS app",
        [("String Catalogs", "https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog"),
         ("String(localized:)", "https://developer.apple.com/documentation/foundation/string/init(localized:)")],
    ))


def project_23():
    name = "StoreKitLab"
    d = ROOT / "23-storekit"
    extra = '''
import StoreKit
''' + todo_block(
        "StoreKit 2 purchase + entitlements",
        "Load products, purchase, and unlock content via Transaction APIs.",
        [
            "Create an StoreKit Configuration file in Xcode (`.storekit`) with a non-consumable product id.",
            "`let products = try await Product.products(for: ids)`",
            "Call `try await product.purchase()` and handle `Product.PurchaseResult`.",
            "On verified success, unlock content and `await transaction.finish()`.",
            "Listen to `Transaction.updates` / use `Transaction.currentEntitlements` to restore state.",
            "Optional SwiftUI: `ProductView` / `StoreView` + `onInAppPurchaseCompletion`.",
        ],
        ["Use StoreKit Testing in Xcode — no App Store Connect product required for local testing.",
         "Never invent receipt-parsing APIs from StoreKit 1."],
        ["Purchasing in the local StoreKit config unlocks a feature flag in the UI."],
        [
            "https://developer.apple.com/documentation/storekit",
            "https://developer.apple.com/documentation/storekit/product",
            "https://developer.apple.com/documentation/storekit/product/purchase(options:)",
            "https://developer.apple.com/documentation/storekit/transaction",
            "https://developer.apple.com/storekit/",
        ],
    )
    sources = app_sources(name, "StoreKit 2", "In-app purchases", "Shop", "\n" + extra)
    write(d / "Products.storekit", '''\
{
  "identifier" : "SwiftLearningStore",
  "nonRenewingSubscriptions" : [],
  "products" : [
    {
      "displayPrice" : "1.99",
      "familyShareable" : false,
      "internalID" : "AAAA1111",
      "localizations" : [
        {
          "description" : "Unlock pro study themes",
          "displayName" : "Pro Themes",
          "locale" : "en_US"
        }
      ],
      "productID" : "com.swiftlearning.storekitlab.prothemes",
      "referenceName" : "Pro Themes",
      "type" : "NonConsumable"
    }
  ],
  "settings" : { "_failTransactionsEnabled" : false },
  "subscriptionGroups" : [],
  "version" : {
    "major" : 3,
    "minor" : 0
  }
}
''')
    generate_xcode_app(d, name, "com.swiftlearning.StoreKitLab", sources)
    write(d / "README.md", readme_project(
        "23", "StoreKit 2 In-App Purchases",
        ["Product.products", "purchase()", "Transaction.finish", "currentEntitlements", "StoreKit Configuration testing"],
        "A tiny shop that unlocks “Pro Themes”.",
        ["Attach Products.storekit to the scheme", "Implement purchase + entitlements UI", "Test cancel/pending paths"],
        ["Subscriptions with SubscriptionStoreView", "Offer codes (advanced)"],
        "Xcode 27 + StoreKit Testing.",
        ["Cannot purchase-test on Linux.", "StoreKit Configuration JSON may need slight tweaks if Xcode migrates the format — let Xcode re-save if it prompts."],
        "Xcode iOS app",
        [("StoreKit", "https://developer.apple.com/documentation/storekit"),
         ("Product.purchase", "https://developer.apple.com/documentation/storekit/product/purchase(options:)"),
         ("Transaction", "https://developer.apple.com/documentation/storekit/transaction")],
    ))


def project_24():
    name = "PushNotificationsLab"
    d = ROOT / "24-push-notifications"
    extra = '''
import UserNotifications
''' + todo_block(
        "Local + remote notification plumbing",
        "Request authorization, register for remote notifications, handle foreground presentation.",
        [
            "Ask for notification permission with `UNUserNotificationCenter`.",
            "Schedule a **local** notification as a first milestone.",
            "Call `UIApplication.shared.registerForRemoteNotifications()` and implement delegate to receive device token.",
            "Document how you’d send a test push via CloudKit / APNs provider / Push Notification Console.",
            "Implement `UNUserNotificationCenterDelegate` for foreground display.",
        ],
        ["Remote pushes need Apple Developer push capability + a server or Push Console.",
         "Start with local notifications so you learn the UX without a server."],
        ["Local notification appears; app logs device token when registered."],
        [
            "https://developer.apple.com/documentation/usernotifications",
            "https://developer.apple.com/documentation/usernotifications/unusernotificationcenter",
            "https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns",
            "https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications",
        ],
    )
    sources = app_sources(name, "Push Notifications", "UserNotifications + APNs", "Push", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.PushNotificationsLab", sources, entitlements=PUSH_ENTITLEMENTS)
    write(d / "README.md", readme_project(
        "24", "Push Notifications",
        ["UNUserNotificationCenter", "Authorization", "Device tokens", "APNs", "Foreground delegation"],
        "Permission flow + local notification + remote registration hooks.",
        ["Implement auth + local schedule", "Enable Push capability with your team", "Capture device token"],
        ["Notification Service Extension for rich media", "ActivityKit push for Live Activities"],
        "Xcode 27 + Developer account for remote push.",
        ["Remote delivery not verifiable here.", "Entitlements use development aps-environment."],
        "Xcode iOS app",
        [("User Notifications", "https://developer.apple.com/documentation/usernotifications"),
         ("Sending to APNs", "https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns")],
    ))


def project_25():
    name = "PerformanceLab"
    d = ROOT / "25-performance"
    extra = todo_block(
        "Find and fix a hitch",
        "Use Instruments to diagnose a deliberately inefficient SwiftUI screen, then fix it.",
        [
            "Build a List of 5_000 items with an intentionally expensive row (e.g. heavy synchronous work in `body`).",
            "Profile with Instruments → SwiftUI / Time Profiler / Hitches (Xcode 27 Instruments workflows).",
            "Move work off the hot path (precompute, cache, simplify view body, use `EquatableView` patterns carefully).",
            "Write a short PERF_NOTES.md: before/after + screenshot names.",
        ],
        ["Prefer fixing algorithmic work before micro-optimizing.",
         "WWDC26 Xcode/Instruments sessions discuss responsiveness tooling."],
        ["Scrolling remains responsive after fix; notes document the measurement."],
        [
            "https://developer.apple.com/documentation/xcode/improving-your-app-s-performance",
            "https://developer.apple.com/videos/play/wwdc2026/258/",
            "https://developer.apple.com/documentation/swiftui/view-performance",
        ],
    )
    sources = app_sources(name, "Performance", "Instruments & hitches", "Perf", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.PerformanceLab", sources)
    write(d / "PERF_NOTES.md", "# Performance notes\n\nFill in after you profile:\n\n- Before:\n- After:\n- Instruments template used:\n- Root cause:\n")
    write(d / "README.md", readme_project(
        "25", "Performance & Instruments",
        ["Time Profiler", "SwiftUI performance", "Main-thread hitches", "Measurement discipline"],
        "A slow list you will make fast, with notes to prove it.",
        ["Implement heavy list", "Profile", "Optimize", "Record notes"],
        ["Memory Graph for leaks", "os_signpost intervals"],
        "Xcode 27 + Instruments on Mac.",
        ["Instruments UI cannot run in this cloud environment."],
        "Xcode iOS app",
        [("Improving your app’s performance", "https://developer.apple.com/documentation/xcode/improving-your-app-s-performance"),
         ("What’s new in Xcode 27 — WWDC26", "https://developer.apple.com/videos/play/wwdc2026/258/")],
    ))


def project_26():
    d = ROOT / "26-swift-macros"
    # Macro packages need special targets — provide a simpler "learn macros" package that uses peer macros via a stub approach
    # Full macro authoring requires a compiler plugin target. Structure it correctly for SwiftPM.
    write(d / "Package.swift", '''\
// swift-tools-version: 6.0
import PackageDescription
import CompilerPluginSupport

let package = Package(
    name: "SwiftMacrosLab",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "SwiftMacrosLab", targets: ["SwiftMacrosLab"]),
        .executable(name: "SwiftMacrosLabCLI", targets: ["SwiftMacrosLabCLI"]),
    ],
    dependencies: [
        .package(url: "https://github.com/swiftlang/swift-syntax.git", from: "600.0.0"),
    ],
    targets: [
        .macro(
            name: "SwiftMacrosLabMacros",
            dependencies: [
                .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
                .product(name: "SwiftCompilerPlugin", package: "swift-syntax"),
            ]
        ),
        .target(name: "SwiftMacrosLab", dependencies: ["SwiftMacrosLabMacros"]),
        .executableTarget(name: "SwiftMacrosLabCLI", dependencies: ["SwiftMacrosLab"]),
        .testTarget(name: "SwiftMacrosLabTests", dependencies: [
            "SwiftMacrosLab",
            "SwiftMacrosLabMacros",
            .product(name: "SwiftSyntaxMacrosGenericTestSupport", package: "swift-syntax"),
        ]),
    ]
)
''')
    write(d / "Sources" / "SwiftMacrosLabMacros" / "SwiftMacrosLabMacros.swift", f'''\
import SwiftCompilerPlugin
import SwiftSyntax
import SwiftSyntaxBuilder
import SwiftSyntaxMacros

/// Freestanding macro `#stringify(expr)` → tuple of (value, source code string).
public struct StringifyMacro: ExpressionMacro {{
    public static func expansion(
        of node: some ExpressionMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) throws -> ExprSyntax {{
{todo_block(
    "Implement #stringify",
    "Return an expression that creates a tuple (value, \"source\").",
    [
        "Read the first argument expression from `node`.",
        "Use `context.locale`? No — use the argument description for the string side.",
        "Classic implementation returns: `( <arg>, \"<arg>\" )` as ExprSyntax.",
    ],
    [
        "Apple sample / SE-0049-style stringify is the usual tutorial macro.",
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/",
    ],
    ["`#stringify(1 + 2)` expands such that `.1` contains `1 + 2`."],
    [
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/",
        "https://developer.apple.com/documentation/swift/macros",
    ],
)}
        // Starter: compile-safe placeholder expansion so the package can build before you implement.
        // Replace with real expansion in solutions / your work.
        return ExprSyntax(stringLiteral: #"(0, "TODO")"#)
    }}
}}

@main
struct SwiftMacrosLabPlugin: CompilerPlugin {{
    let providingMacros: [Macro.Type] = [StringifyMacro.self]
}}
''')
    write(d / "Sources" / "SwiftMacrosLab" / "SwiftMacrosLab.swift", '''\
@freestanding(expression)
public macro stringify<T>(_ value: T) -> (T, String) = #externalMacro(module: "SwiftMacrosLabMacros", type: "StringifyMacro")
''')
    write(d / "Sources" / "SwiftMacrosLabCLI" / "main.swift", '''\
import SwiftMacrosLab

let pair = #stringify(1 + 2)
print(pair)
''')
    write(d / "Tests" / "SwiftMacrosLabTests" / "SwiftMacrosLabTests.swift", '''\
import Testing
import SwiftMacrosLab

@Test func stringifyCompiles() {
    let pair = #stringify(2)
    #expect(pair.0 == 2)
}
''')
    write(d / "README.md", readme_project(
        "26", "Swift Macros & Authoring Packages",
        ["Freestanding macros", "CompilerPlugin", "SwiftSyntax", "Macro test strategies"],
        "A `#stringify` macro package (starter expands to a placeholder until you implement it).",
        ["Study macro target layout", "Implement StringifyMacro.expansion", "Run CLI + tests"],
        ["Add an `@attached(member)` macro that synthesizes an `init`"],
        "Xcode 16+ / Swift 6; Linux may build if swift-syntax resolves (network).",
        [
            "First `swift build` downloads swift-syntax — needs network.",
            "Macro expansion tests using SwiftSyntaxMacrosGenericTestSupport may need adjustment per swift-syntax version.",
            "Starter macro intentionally returns a placeholder tuple so scaffolding compiles before the TODO is done.",
        ],
        "Swift Package (macro + library + CLI)",
        [("Macros (TSL)", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/"),
         ("Swift Macros", "https://developer.apple.com/documentation/swift/macros")],
    ))


def project_27():
    name = "MacNotes"
    d = ROOT / "27-macos-app"
    extra = todo_block(
        "macOS multi-window SwiftUI app",
        "Build a Notes-style Mac app with NavigationSplitView and a Settings scene.",
        [
            "Use `NavigationSplitView` for sidebar + detail.",
            "Add a `Settings` scene with a Toggle.",
            "Support keyboard shortcut ⌘N for new note (`commands` / Button shortcut).",
            "Consider macOS inactive window appearance (`appearsActive` env) from WWDC26 SwiftUI guidance.",
        ],
        ["Target macOS 14+; Xcode 27 for latest Liquid Glass on Mac."],
        ["Sidebar selection updates detail; Settings opens from app menu."],
        [
            "https://developer.apple.com/documentation/swiftui/navigationsplitview",
            "https://developer.apple.com/documentation/swiftui/settings",
            "https://developer.apple.com/videos/play/wwdc2026/269/",
        ],
    )
    sources = app_sources(name, "macOS App", "NavigationSplitView + Settings", "MacNotes", "\n" + extra)
    # Generate as macOS by tweaking — reuse generator with macos platforms string
    generate_xcode_app(
        d, name, "com.swiftlearning.MacNotes", sources,
        deployment="14.0",
        platforms="macosx",
    )
    # Fix Info.plist LSRequiresIPhoneOS — rewrite app Info for Mac
    write(d / name / "Info.plist", '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleName</key>
	<string>MacNotes</string>
	<key>CFBundleDisplayName</key>
	<string>MacNotes</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleVersion</key>
	<string>1</string>
</dict>
</plist>
''')
    write(d / "README.md", readme_project(
        "27", "macOS App",
        ["NavigationSplitView", "Settings scene", "Commands / shortcuts", "macOS windowing"],
        "A multi-pane Mac notes shell.",
        ["Open in Xcode as a Mac run destination", "Implement split view + settings + ⌘N"],
        ["Menu bar extra", "DocumentGroup / new Document APIs from WWDC26"],
        "Xcode 27 / macOS 27 SDK recommended (deployment 14+ OK for basics).",
        [
            "Committed pbxproj may still list iOS SDK defaults in some build settings — set the run destination to My Mac and fix TARGETED_DEVICE_FAMILY / SDKROOT in Xcode if needed (or regenerate with XcodeGen and macOS platform).",
            "Not buildable on Linux.",
        ],
        "Xcode macOS app (verify destination on open)",
        [("NavigationSplitView", "https://developer.apple.com/documentation/swiftui/navigationsplitview"),
         ("Settings", "https://developer.apple.com/documentation/swiftui/settings")],
    ))


def project_28():
    name = "WatchCompanion"
    d = ROOT / "28-watchos-companion"
    write(d / "README.md", readme_project(
        "28", "watchOS Companion",
        ["watchOS SwiftUI lifecycle", "Shared model via App Group / WatchConnectivity", "Complications (optional)"],
        "A watchOS timer companion that mirrors a simple iOS host counter.",
        [
            "On Mac with Xcode: File → New → Project → iOS App + watchOS App (or add Watch App target to the provided host).",
            "Implement a shared Int counter using App Groups UserDefaults **or** WatchConnectivity.",
            "Show the value on both iOS and watchOS UIs.",
            "Optional: circular complication.",
        ],
        ["Independent watchOS app (no phone) variant"],
        "Xcode 27 with watchOS SDK; hardware Watch optional (simulator OK).",
        [
            "Full dual-target project generation is brittle without Xcode — this folder ships an **iOS host scaffold** plus instructions to add the Watch target.",
            "Apple-only; untested here.",
        ],
        "Xcode iOS host + (you add) watchOS app target",
        [("watchOS apps", "https://developer.apple.com/documentation/watchos-apps"),
         ("Watch Connectivity", "https://developer.apple.com/documentation/watchconnectivity"),
         ("SwiftUI on watchOS", "https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps/")],
    ))
    sources = app_sources(name, "watchOS Companion Host", "Add Watch target in Xcode", "Host", "\n" + todo_block(
        "Shared counter with Watch",
        "Mirror a counter to a Watch app you add in Xcode.",
        ["Add Watch App target", "Share data via App Group or WatchConnectivity", "Update both UIs"],
        ["Prefer simple App Group Int for the first milestone."],
        ["Changing value on phone updates watch within a few seconds (or sooner)."],
        ["https://developer.apple.com/documentation/watchconnectivity"],
    ))
    generate_xcode_app(d, name, "com.swiftlearning.WatchCompanion", sources)


def project_29():
    name = "LiquidGlassIOS27"
    d = ROOT / "29-liquid-glass-ios27"
    extra = todo_block(
        "Adopt Liquid Glass + iOS 27 SwiftUI APIs",
        "Build a resizable, glass-polished starter that uses verified iOS 26/27 APIs.",
        [
            "Apply `.glassEffect(_:in:)` to a custom control; prefer `.buttonStyle(.glass)` for buttons.",
            "Group related glass views in `GlassEffectContainer` when using multiple effects.",
            "Try toolbar APIs from WWDC26: `visibilityPriority`, `ToolbarOverflowMenu`, `toolbarMinimizeBehavior`.",
            "Exercise resizability (iPhone apps are resizable in iOS 27 — test with Live Preview resize handles / iPhone Mirroring).",
            "Optional: `Tab(role: .prominent)` for a distinct tab.",
        ],
        [
            "Liquid Glass landed broadly with iOS 26; iOS 27 refreshes it further — standard components adopt automatically when building with latest SDK.",
            "Do not invent glass APIs; confirm `.glassEffect` in your SDK docs.",
        ],
        ["UI shows glass styling; toolbar behavior remains usable when the window is narrow."],
        [
            "https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass",
            "https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)",
            "https://developer.apple.com/documentation/technologyoverviews/liquid-glass",
            "https://developer.apple.com/videos/play/wwdc2026/269/",
            "https://developer.apple.com/videos/play/wwdc2026/278/",
        ],
    ) + '''
/*
 Example shapes (verify in SDK):
   Text("Hello")
     .padding()
     .glassEffect(.regular, in: .rect(cornerRadius: 16))

 Gate if you support older OS:
   if #available(iOS 26, *) { ... } else { ... material fallback ... }
*/
'''
    sources = app_sources(name, "Liquid Glass & iOS 27", "Design + new SwiftUI APIs", "Glass", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.LiquidGlassIOS27", sources, deployment="26.0")
    write(d / "README.md", readme_project(
        "29", "Latest OS APIs & Liquid Glass",
        ["Liquid Glass (glassEffect / glass button styles)", "Toolbar overflow & visibilityPriority", "iOS 27 resizability", "Prominent tabs"],
        "A small showcase app for modern system design + WWDC26 SwiftUI additions.",
        ["Build with iOS 27 SDK", "Implement glass + toolbar TODOs", "Resize preview / mirroring test"],
        ["Document APIs from WWDC26 session 269 (AsyncImage caching, ContentBuilder notes)",
         "Explore new Document protocols if you extend into documents"],
        "**Xcode 27** + iOS 27 SDK (deployment 26+ for glass APIs).",
        [
            "Not compile-verified here.",
            "Some WWDC26 toolbar symbol names (`ToolbarOverflowMenu`, `visibilityPriority`, `topBarPinnedTrailing`) are taken from Apple’s WWDC26 session transcript — confirm exact spellings/availability in your installed SDK documentation before shipping.",
            "Liquid Glass overview: https://developer.apple.com/documentation/technologyoverviews/liquid-glass",
        ],
        "Xcode iOS app",
        [("Adopting Liquid Glass", "https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass"),
         ("glassEffect", "https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)"),
         ("What’s new in SwiftUI — WWDC26", "https://developer.apple.com/videos/play/wwdc2026/269/")],
    ))


def project_30():
    d = ROOT / "30-ci-release"
    write(d / "README.md", readme_project(
        "30", "CI, TestFlight & App Store Release",
        ["Xcode Cloud workflows", "fastlane alternative", "TestFlight", "App Store Connect metadata", "Export compliance / privacy"],
        "A release playbook + sample config stubs you will customize for one of your earlier apps.",
        [
            "Pick one app project (e.g. 12 or 31) as the release candidate",
            "Fill `RELEASE_CHECKLIST.md`",
            "Either configure Xcode Cloud (`ci_scripts` / workflow in App Store Connect) **or** adapt the sample Fastfile",
            "Create a TestFlight internal build",
            "Draft App Store listing fields (no need to submit publicly)",
        ],
        ["Automated UI tests in CI", "Marketing screenshots via Xcode"],
        "Xcode 27 + Apple Developer Program membership.",
        [
            "No real App Store Connect push from this environment.",
            "Xcode Cloud requires linking the GitHub repo in Apple Developer portals.",
            "fastlane needs Ruby gems + credentials — treat sample as a template.",
        ],
        "Documentation + CI templates (no runnable iOS build here)",
        [("Xcode Cloud", "https://developer.apple.com/xcode-cloud/"),
         ("TestFlight", "https://developer.apple.com/testflight/"),
         ("Distributing your app for beta testing and releases", "https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases"),
         ("fastlane docs", "https://docs.fastlane.tools/")],
    ))
    write(d / "RELEASE_CHECKLIST.md", '''\
# Release checklist

- [ ] Bundle ID finalized + App ID created
- [ ] Version / build numbers bumped
- [ ] Privacy Nutrition Labels drafted
- [ ] App Privacy Policy URL ready (if needed)
- [ ] Export compliance answered
- [ ] Screenshots for required device sizes
- [ ] Internal TestFlight group created
- [ ] CI builds on tag / main
- [ ] Crash reporting symbol upload (if used)
- [ ] Final QA on physical device

## Notes

Record your chosen distribution path: **Xcode Cloud** / **fastlane** / **manual archive**.
''')
    write(d / "ci_scripts" / "ci_post_clone.sh", '''\
#!/bin/sh
set -e
# Xcode Cloud post-clone hook (example)
echo "ci_post_clone: add dependency installs here if needed"
''')
    write(d / "fastlane" / "Fastfile", '''\
default_platform(:ios)

platform :ios do
  desc "Build and upload to TestFlight (template — configure with your team/app identifiers)"
  lane :beta do
    # build_app(scheme: "YourScheme")
    # upload_to_testflight(skip_waiting_for_build_processing: true)
    UI.important("Template lane — uncomment and set scheme/bundle IDs before use.")
  end
end
''')
    write(d / "fastlane" / "Appfile", '''\
# app_identifier("com.swiftlearning.YourApp")
# apple_id("you@example.com")
# team_id("YOURTEAMID")
''')


def project_31():
    name = "Capstone"
    d = ROOT / "31-capstone"
    extra = todo_block(
        "Capstone: StudyPilot",
        "Ship a multi-feature study planner that combines the course pillars.",
        [
            "Domain: subjects + study sessions (SwiftData).",
            "Optional sync: SwiftData+CloudKit private DB (from 14) — skip sharing unless you also apply 15.",
            "Networking: fetch an inspirational quote JSON (reuse 11 patterns) with Codable.",
            "Architecture: modularize Core + Features (from 17) or clear MVVM boundaries + Swift Testing (16).",
            "Surface: Widget **or** App Intent **or** Foundation Models summary (pick ≥2 from 18/19/20).",
            "Polish: accessibility (21), localization (22), Liquid Glass styling (29).",
            "Stretch: StoreKit tip jar (23) + TestFlight via 30.",
        ],
        ["Prefer depth over checkbox tourism — a coherent app beats stubbing every framework.",
         "Document architecture decisions in ARCHITECTURE.md."],
        [
            "App builds in Xcode 27 for iOS 27.",
            "At least one automated test suite passes.",
            "ARCHITECTURE.md explains module boundaries + data flow.",
            "README demo section lists features you actually finished.",
        ],
        [
            "https://developer.apple.com/documentation/swiftdata",
            "https://developer.apple.com/documentation/swiftui",
            "https://developer.apple.com/documentation/foundationmodels",
            "https://developer.apple.com/documentation/appintents",
            "https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass",
        ],
    )
    sources = app_sources(name, "Capstone — StudyPilot", "Combine the course into one app", "StudyPilot", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.Capstone", sources, deployment="26.0", entitlements=CLOUDKIT_ENTITLEMENTS)
    write(d / "ARCHITECTURE.md", '''\
# StudyPilot architecture

Fill this in as you build:

## Modules / folders

## Data flow

## Persistence & sync

## Why this boundary

## Test strategy
''')
    write(d / "README.md", readme_project(
        "31", "Capstone — StudyPilot",
        ["Product thinking", "Integration of prior projects", "Architecture docs", "Polish for humans"],
        "Your own StudyPilot app proving pro-level iOS skills.",
        ["Outline MVP in ARCHITECTURE.md", "Implement vertical slice", "Add tests + polish", "Optional TestFlight"],
        ["watchOS complications", "Shared CloudKit zone with a study buddy (project 15 techniques)"],
        "**Xcode 27** / iOS 27 SDK.",
        ["Entire capstone is Apple-platform; not verified on Linux.", "CloudKit entitlement placeholder must be replaced."],
        "Xcode iOS app",
        [("SwiftUI", "https://developer.apple.com/documentation/swiftui"),
         ("SwiftData", "https://developer.apple.com/documentation/swiftdata"),
         ("Adopting Liquid Glass", "https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass")],
    ))


def main():
    print("Generating 17-31...")
    for fn in [
        project_17, project_18, project_19, project_20, project_21, project_22,
        project_23, project_24, project_25, project_26, project_27, project_28,
        project_29, project_30, project_31,
    ]:
        fn()
    print("17-31 done")


if __name__ == "__main__":
    main()
