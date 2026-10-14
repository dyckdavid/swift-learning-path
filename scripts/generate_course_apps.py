#!/usr/bin/env python3
"""Generate app / advanced projects 06–31 for the Swift Learning Path."""

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

CLOUDKIT_ENTITLEMENTS = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.developer.icloud-container-identifiers</key>
	<array>
		<string>iCloud.com.swiftlearning.REPLACE_ME</string>
	</array>
	<key>com.apple.developer.icloud-services</key>
	<array>
		<string>CloudKit</string>
	</array>
	<key>com.apple.developer.ubiquity-kvstore-identifier</key>
	<string>$(TeamIdentifierPrefix)$(CFBundleIdentifier)</string>
</dict>
</plist>
'''

PUSH_ENTITLEMENTS = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>aps-environment</key>
	<string>development</string>
</dict>
</plist>
'''


def project_06():
    name = "SwiftUIBasics"
    d = ROOT / "06-swiftui-basics"
    extra = todo_block(
        "Compose your first screen",
        "Replace the placeholder VStack with a profile card layout.",
        [
            "Add an Image (systemName: \"person.circle.fill\"), name Text, and a short bio.",
            "Use VStack/HStack/ZStack and padding/spacing.",
            "Apply font and foregroundStyle modifiers.",
        ],
        ["SF Symbols work offline via Image(systemName:).", "Keep everything in ContentView for now."],
        ["Builds and shows a readable single-screen composition on iPhone simulator."],
        [
            "https://developer.apple.com/documentation/swiftui",
            "https://developer.apple.com/documentation/swiftui/vstack",
            "https://developer.apple.com/tutorials/swiftui",
        ],
    )
    sources = app_sources(name, "SwiftUI Basics", "Layout, views, modifiers", "Basics", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.SwiftUIBasics", sources)
    write(d / "README.md", readme_project(
        "06", "SwiftUI Basics",
        ["View protocol", "Stacks & layout", "Modifiers", "Previews"],
        "A single-screen SwiftUI profile card.",
        ["Open the .xcodeproj in Xcode", "Run on Simulator", "Implement the TODO layout"],
        ["Add a dark/light-friendly hierarchical ShapeStyle", "Extract a ProfileHeader subview"],
        "**Xcode 27** recommended (iOS 27 SDK). Minimum conceptually iOS 17+ / Xcode 16+.",
        ["Cannot compile SwiftUI iOS apps on Linux — open in Xcode on a Mac.",
         "Committed .xcodeproj was generated without Xcode; if it misbehaves, regenerate with `xcodegen` from project.yml."],
        "Xcode iOS app (SwiftUI) + project.yml",
        [("SwiftUI", "https://developer.apple.com/documentation/swiftui"),
         ("SwiftUI Tutorials", "https://developer.apple.com/tutorials/swiftui")],
    ))


def project_07():
    name = "NavigationLists"
    d = ROOT / "07-navigation-lists"
    extra = '''
struct SampleItem: Identifiable, Hashable {
    let id: UUID
    var title: String
    init(title: String) { self.id = UUID(); self.title = title }
}

enum SampleData {
    static let items: [SampleItem] = [
        .init(title: "NavigationStack"),
        .init(title: "List"),
        .init(title: "NavigationLink"),
    ]
}
''' + todo_block(
        "List + NavigationStack detail",
        "Show SampleData.items in a List and push a detail screen.",
        [
            "Use NavigationStack + List(SampleData.items).",
            "Each row is a NavigationLink to a detail view showing the title.",
            "Support swipe-to-delete OR a toolbar EditButton (your choice).",
        ],
        ["Prefer value-based NavigationLink(value:) + navigationDestination(for:).",
         "WWDC26 adds richer reorder APIs — optional stretch; see docs."],
        ["Tapping a row shows detail; back navigation works."],
        [
            "https://developer.apple.com/documentation/swiftui/navigationstack",
            "https://developer.apple.com/documentation/swiftui/list",
            "https://developer.apple.com/videos/play/wwdc2026/269/",
        ],
    )
    sources = app_sources(name, "Navigation & Lists", "Stack navigation + List", "Library", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.NavigationLists", sources)
    write(d / "README.md", readme_project(
        "07", "Navigation & Lists",
        ["NavigationStack", "List / Identifiable", "NavigationLink values", "Optional reordering (iOS 27)"],
        "A master-detail list of learning topics.",
        ["Wire List + detail destination", "Try edit/delete"],
        ["Adopt reorderable container APIs from WWDC26 if targeting iOS 27+",
         "https://developer.apple.com/videos/play/wwdc2026/269/"],
        "Xcode 27 / iOS 27 SDK recommended.",
        ["Linux untested (SwiftUI).", "Reorder APIs require iOS 27 — flag if you stay on older OS."],
        "Xcode iOS app",
        [("NavigationStack", "https://developer.apple.com/documentation/swiftui/navigationstack"),
         ("What’s new in SwiftUI — WWDC26", "https://developer.apple.com/videos/play/wwdc2026/269/")],
    ))


def project_08():
    name = "StateObservation"
    d = ROOT / "08-state-observation"
    extra = '''
import Observation

@Observable
final class CounterModel {
    var count: Int = 0
    // TODO: add reset() and increment(by:)
}
''' + todo_block(
        "Observation & bindings",
        "Drive the UI from an @Observable model and two-way bindings.",
        [
            "Hold `@State private var model = CounterModel()` in ContentView.",
            "Show count, buttons to increment/reset.",
            "Add a Toggle bound to a `isHighlighted` Bool on the model (add the property).",
            "Remember: @State for Observable classes is lazily initialized on newer SDKs (WWDC26 / back-deployed).",
        ],
        ["Prefer @Observable over ObservableObject for new code.",
         "Use Bindable(model) when you need bindings to observable properties."],
        ["UI updates when count changes without manual objectWillChange."],
        [
            "https://developer.apple.com/documentation/observation",
            "https://developer.apple.com/documentation/observation/observable()",
            "https://developer.apple.com/documentation/swiftui/bindable",
            "https://developer.apple.com/videos/play/wwdc2026/269/",
        ],
    )
    sources = app_sources(name, "State & Observation", "@Observable, @State, bindings", "Counter", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.StateObservation", sources)
    write(d / "README.md", readme_project(
        "08", "State & Observation",
        ["@Observable", "@State / @Bindable", "Unidirectional UI updates", "Lazy @State class init (WWDC26 note)"],
        "A counter app powered by Observation.",
        ["Complete CounterModel", "Bind Toggle + buttons"],
        ["Split model into a store shared via environment"],
        "Xcode 27 recommended; Observation available since iOS 17.",
        ["Linux untested."],
        "Xcode iOS app",
        [("Observation", "https://developer.apple.com/documentation/observation"),
         ("Observable()", "https://developer.apple.com/documentation/observation/observable()")],
    ))


def project_09():
    name = "FormsLab"
    d = ROOT / "09-forms"
    extra = todo_block(
        "Build a settings form",
        "Create a Form with text fields, picker, toggle, and validation.",
        [
            "Fields: display name (TextField), difficulty (Picker), notifications (Toggle).",
            "Disable a Save button until name.trimmingCharacters is non-empty.",
            "On Save, present an alert confirming values.",
        ],
        ["Use @State properties.", "Form {{ Section {{ ... }} }}"],
        ["Save disabled for blank names; alert shows submitted values."],
        ["https://developer.apple.com/documentation/swiftui/form",
         "https://developer.apple.com/documentation/swiftui/textfield"],
    )
    sources = app_sources(name, "Forms", "Inputs & validation", "Profile", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.FormsLab", sources)
    write(d / "README.md", readme_project(
        "09", "Forms & Data Entry",
        ["Form / Section", "TextField / Picker / Toggle", "Simple validation", "Alerts"],
        "A profile/settings form with a validated save action.",
        ["Implement form UI + alert"],
        ["Add `@FocusState` keyboard management"],
        "Xcode 27 recommended.",
        ["Linux untested."],
        "Xcode iOS app",
        [("Form", "https://developer.apple.com/documentation/swiftui/form")],
    ))


def project_10():
    name = "AnimationsLab"
    d = ROOT / "10-animations"
    extra = todo_block(
        "Implicit & explicit animation",
        "Animate a shape’s size, color, and a transition.",
        [
            "Add a Circle that grows when a button is tapped (`withAnimation`).",
            "Toggle a detail view with `.transition(.move(edge: .bottom).combined(with: .opacity))`.",
            "Try `.symbolEffect(.bounce)` on an SF Symbol (iOS 17+).",
        ],
        ["Prefer `withAnimation(.spring)` for playful motion.", "Keep motion intentional (2–3 effects)."],
        ["Taps animate size; detail appears/disappears with transition."],
        ["https://developer.apple.com/documentation/swiftui/animation",
         "https://developer.apple.com/documentation/swiftui/view/transition(_:)",
         "https://developer.apple.com/documentation/swiftui/view/symboleffect(_:options:value:)"],
    )
    sources = app_sources(name, "Animations", "Motion & transitions", "Motion", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.AnimationsLab", sources)
    write(d / "README.md", readme_project(
        "10", "Animations & Transitions",
        ["withAnimation", "transitions", "symbolEffect", "springs"],
        "A playful motion playground.",
        ["Animate circle + transition + symbol"],
        ["Matched geometry effect between two screens"],
        "Xcode 27 recommended.",
        ["Linux untested."],
        "Xcode iOS app",
        [("Animation", "https://developer.apple.com/documentation/swiftui/animation")],
    ))


def project_11():
    d = ROOT / "11-networking-codable"
    name = "NetworkingCodable"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "NetworkingCodable.swift", f'''\
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

public struct RemotePost: Codable, Equatable, Sendable, Identifiable {{
    public let id: Int
    public let title: String
    public let body: String
}}

public protocol HTTPSession: Sendable {{
    func data(for request: URLRequest) async throws -> (Data, URLResponse)
}}

extension URLSession: HTTPSession {{
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {{
        #if canImport(FoundationNetworking)
        try await withCheckedThrowingContinuation {{ (cont: CheckedContinuation<(Data, URLResponse), Error>) in
            let task = self.dataTask(with: request) {{ data, response, error in
                if let error {{
                    cont.resume(throwing: error)
                }} else if let data, let response {{
                    cont.resume(returning: (data, response))
                }} else {{
                    cont.resume(throwing: URLError(.badServerResponse))
                }}
            }}
            task.resume()
        }}
        #else
        try await self.data(for: request)
        #endif
    }}
}}

public struct PostClient: Sendable {{
    private let session: any HTTPSession
    private let baseURL: URL

    public init(session: any HTTPSession = URLSession.shared, baseURL: URL = URL(string: "https://jsonplaceholder.typicode.com")!) {{
        self.session = session
        self.baseURL = baseURL
    }}

{todo_block(
    "Codable + URLSession",
    "Fetch and decode an array of posts.",
    [
        "Implement `fetchPosts()` using async/await.",
        "Build URL by appending path `posts`.",
        "Validate HTTP status 200..<300.",
        "Decode `[RemotePost]` with `JSONDecoder`.",
    ],
    ["Inject `HTTPSession` so tests can use a fake.", "Do not invent custom JSON keys — models match the API."],
    ["Returns non-empty posts from the public sample API when online.", "Unit test uses fixture data without network."],
    [
        "https://developer.apple.com/documentation/foundation/urlsession",
        "https://developer.apple.com/documentation/foundation/codable",
        "https://developer.apple.com/documentation/foundation/jsondecoder",
    ],
)}
    // public func fetchPosts() async throws -> [RemotePost] {{ fatalError("TODO") }}
}}

public struct FixtureSession: HTTPSession, Sendable {{
    public var data: Data
    public var statusCode: Int
    public init(data: Data, statusCode: Int = 200) {{
        self.data = data
        self.statusCode = statusCode
    }}
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {{
        let response = HTTPURLResponse(url: request.url!, statusCode: statusCode, httpVersion: nil, headerFields: nil)!
        return (data, response)
    }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", "import NetworkingCodable\nprint(\"Implement fetchPosts() then call it from main with await.\")\n")
    write(d / "Tests" / f"{name}Tests" / "NetworkingCodableTests.swift", '''\
import Foundation
import Testing
@testable import NetworkingCodable

@Test func fixtureRoundTrip() throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let posts = try JSONDecoder().decode([RemotePost].self, from: json)
    #expect(posts.first?.id == 1)
}
''')
    write(d / "README.md", readme_project(
        "11", "Networking + Codable",
        ["URLSession async APIs", "Codable / JSONDecoder", "Protocol-based test doubles", "HTTP status handling"],
        "A PostClient against JSONPlaceholder (or fixtures).",
        ["Implement fetchPosts", "Test with FixtureSession", "Optional: run CLI live fetch"],
        ["Add createPost with POST + encode", "Map errors to a domain enum"],
        "Xcode 16+ / Swift 6; **Linux `swift test` OK** for fixtures.",
        ["Live network calls depend on jsonplaceholder.typicode.com availability."],
        "Swift Package",
        [("URLSession", "https://developer.apple.com/documentation/foundation/urlsession"),
         ("Codable", "https://developer.apple.com/documentation/foundation/codable")],
    ))


def project_12():
    name = "SwiftDataLab"
    d = ROOT / "12-swiftdata"
    extra = '''
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
''' + todo_block(
        "SwiftData CRUD list",
        "Persist notes with SwiftData and show them in a List.",
        [
            "Uncomment the Note @Model.",
            "Attach `.modelContainer(for: Note.self)` to the App (or WindowGroup content).",
            "Use @Query to list notes; toolbar button inserts a note; swipe deletes.",
        ],
        ["Start with an in-memory configuration for Previews.",
         "https://developer.apple.com/documentation/swiftdata/modelcontainer"],
        ["Notes persist across launches on device/simulator (disk config)."],
        [
            "https://developer.apple.com/documentation/swiftdata",
            "https://developer.apple.com/documentation/swiftdata/model()",
            "https://developer.apple.com/documentation/swiftdata/query",
        ],
    )
    sources = app_sources(name, "SwiftData", "Local persistence", "Notes", "\n" + extra)
    # Fix App file to mention modelContainer in TODO via separate file note
    sources["SwiftDataLabApp.swift"] = '''\
import SwiftUI
import SwiftData

@main
struct SwiftDataLabApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // .modelContainer(for: Note.self) // TODO: enable after defining Note
    }
}
'''
    generate_xcode_app(d, name, "com.swiftlearning.SwiftDataLab", sources)
    write(d / "README.md", readme_project(
        "12", "SwiftData (Local)",
        ["@Model", "ModelContainer", "@Query", "Insert/delete"],
        "A Notes list backed by SwiftData.",
        ["Define Note", "Wire modelContainer", "Build CRUD UI"],
        ["Add #Predicate filtering", "Sort descriptors"],
        "Xcode 27 / iOS 17+ (SwiftData).",
        ["Linux untested — SwiftData is Apple platforms only."],
        "Xcode iOS app",
        [("SwiftData", "https://developer.apple.com/documentation/swiftdata"),
         ("ModelConfiguration", "https://developer.apple.com/documentation/swiftdata/modelconfiguration")],
    ))


def project_13():
    name = "CloudKitFundamentals"
    d = ROOT / "13-cloudkit-fundamentals"
    extra = '''
import CloudKit

enum CloudKitPlayground {
    /// Replace with your container ID after enabling iCloud in Signing & Capabilities.
    static let containerID = "iCloud.com.swiftlearning.REPLACE_ME"

    static var container: CKContainer { CKContainer(identifier: containerID) }
    static var privateDB: CKDatabase { container.privateCloudDatabase }
    static var publicDB: CKDatabase { container.publicCloudDatabase }
}
''' + todo_block(
        "Private vs public database write/read",
        "Save a CKRecord to the private DB and fetch it back; understand public DB use cases.",
        [
            "Create a CKRecord(recordType: \"Idea\") with a \"text\" string field.",
            "`try await privateDB.save(record)`.",
            "Fetch with `record(for:)` using the saved recordID.",
            "Write a short comment in code: when would you use publicCloudDatabase instead?",
        ],
        ["You need a real Apple Developer team + iCloud capability for device/simulator signed-in iCloud.",
         "Simulator iCloud sign-in is required.",
         "Start in Development environment in CloudKit Console."],
        ["Save/fetch succeeds when container + iCloud account are configured."],
        [
            "https://developer.apple.com/documentation/cloudkit",
            "https://developer.apple.com/documentation/cloudkit/ckcontainer",
            "https://developer.apple.com/documentation/cloudkit/ckdatabase",
            "https://developer.apple.com/documentation/cloudkit/ckrecord",
        ],
    )
    sources = app_sources(name, "CloudKit", "Private & public databases", "CloudKit", "\n" + extra)
    generate_xcode_app(
        d, name, "com.swiftlearning.CloudKitFundamentals", sources,
        entitlements=CLOUDKIT_ENTITLEMENTS,
    )
    write(d / "README.md", readme_project(
        "13", "CloudKit Fundamentals",
        ["CKContainer", "privateCloudDatabase vs publicCloudDatabase", "CKRecord save/fetch", "iCloud capability"],
        "A minimal Idea record writer/reader using CloudKit directly.",
        ["Enable iCloud/CloudKit capability with your team", "Replace container ID", "Implement save/fetch TODO"],
        ["Query records with CKQuery", "Observe CKAccountStatus"],
        "Xcode 27 + paid Apple Developer account for CloudKit; iCloud-signed simulator/device.",
        [
            "Cannot be compile-verified here (no Xcode / no Apple cloud credentials).",
            "Entitlements use a placeholder container ID — replace before running.",
            "Public DB writes require careful security roles in CloudKit Dashboard.",
        ],
        "Xcode iOS app + CloudKit entitlements",
        [("CloudKit", "https://developer.apple.com/documentation/cloudkit"),
         ("CKDatabase", "https://developer.apple.com/documentation/cloudkit/ckdatabase")],
    ))


def project_14():
    name = "SwiftDataCloudKit"
    d = ROOT / "14-swiftdata-cloudkit"
    extra = '''
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
''' + todo_block(
        "SwiftData ↔ CloudKit private sync",
        "Mirror tasks across devices using SwiftData’s CloudKit integration (private database).",
        [
            "Uncomment SyncedTask @Model.",
            "Create ModelConfiguration(cloudKitDatabase: .automatic) or .private(\"iCloud.com…\").",
            "Build ModelContainer(for: SyncedTask.self, configurations: config).",
            "Run on two signed-in devices/simulators and confirm sync.",
        ],
        [
            "SwiftData+CloudKit syncs the **private** database; it does **not** natively support CKShare user-to-user sharing (confirmed by Apple DTS / forums as of WWDC26).",
            "Bundle ID + container must match entitlements.",
        ],
        ["Records created on device A appear on device B when both use same iCloud account."],
        [
            "https://developer.apple.com/documentation/swiftdata/modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:)",
            "https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase",
            "https://developer.apple.com/documentation/swiftdata",
        ],
    )
    sources = app_sources(name, "SwiftData + CloudKit", "Private DB sync", "Tasks", "\n" + extra)
    sources["SwiftDataCloudKitApp.swift"] = '''\
import SwiftUI
import SwiftData

@main
struct SwiftDataCloudKitApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        // TODO: attach ModelContainer with cloudKitDatabase configuration
    }
}
'''
    generate_xcode_app(d, name, "com.swiftlearning.SwiftDataCloudKit", sources, entitlements=CLOUDKIT_ENTITLEMENTS)
    write(d / "README.md", readme_project(
        "14", "SwiftData + CloudKit Sync",
        ["ModelConfiguration.CloudKitDatabase", "Private sync", "Multi-device testing", "Limitations vs sharing"],
        "Synced task list via SwiftData’s CloudKit private database integration.",
        ["Enable CloudKit", "Configure ModelContainer", "Verify multi-device sync"],
        ["Handle sync conflicts / dense updates thoughtfully"],
        "Xcode 27 + iCloud capability + Developer account.",
        [
            "Apple-only; not verified in this Linux environment.",
            "**API uncertainty / limitation:** SwiftData+CloudKit does not natively support CKShare-style collaborative sharing as of WWDC26 (use project 15 for sharing).",
            "See: https://developer.apple.com/forums/thread/829707",
        ],
        "Xcode iOS app",
        [("ModelConfiguration", "https://developer.apple.com/documentation/swiftdata/modelconfiguration"),
         ("CloudKitDatabase", "https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase")],
    ))


def project_15():
    name = "CloudKitSharing"
    d = ROOT / "15-cloudkit-sharing"
    extra = '''
import CloudKit
import SwiftUI

/// Sharing requires CloudKit (CKShare) or Core Data + NSPersistentCloudKitContainer.
/// SwiftData does not natively support CKShare as of WWDC26 — see README.
''' + todo_block(
        "Create and present a CKShare",
        "Share a root CKRecord with another iCloud user via share URL / share UI.",
        [
            "Ensure shareable records live in a **custom zone** in the private database.",
            "Create `CKShare(rootRecord:)` (hierarchy) or `CKShare(recordZoneID:)` (zone share).",
            "Save share + root together with `modifyRecords(saving:deleting:)`.",
            "Present sharing UI (e.g. `UICloudSharingController` / `CloudSharingView` where available) or distribute `share.url`.",
            "Accept share on a second account and read from `sharedCloudDatabase`.",
        ],
        [
            "Follow Apple’s CloudKit sharing guidance carefully — this is the hardest CloudKit topic.",
            "Core Data path: `NSPersistentCloudKitContainer` sharing sample from Apple is a valid alternative.",
        ],
        ["Second iCloud account can see shared records in sharedCloudDatabase."],
        [
            "https://developer.apple.com/documentation/cloudkit/ckshare",
            "https://developer.apple.com/documentation/cloudkit/sharedcloudkitcontainer",
            "https://developer.apple.com/videos/play/tech-talks/10874/",
            "https://developer.apple.com/documentation/coredata/sharing_core_data_objects_between_icloud_users",
        ],
    )
    sources = app_sources(name, "CloudKit Sharing", "CKShare & shared DB", "Sharing", "\n" + extra)
    generate_xcode_app(d, name, "com.swiftlearning.CloudKitSharing", sources, entitlements=CLOUDKIT_ENTITLEMENTS)
    write(d / "README.md", readme_project(
        "15", "CloudKit Sharing (CKShare)",
        ["CKShare", "sharedCloudDatabase", "Custom zones", "Optional Core Data sharing stack"],
        "Invite another user to a shared record hierarchy or zone.",
        ["Implement share creation", "Test with two Apple IDs", "Read accepted shares from shared DB"],
        ["Zone-wide share vs root-record hierarchy", "Participant permissions"],
        "Xcode 27 + two iCloud accounts + Developer account.",
        [
            "Not verified in CI/Linux.",
            "**Verified limitation:** SwiftData+CloudKit has no native CKShare support as of WWDC26; this project uses CloudKit (or Core Data) APIs instead.",
            "UICloudSharingController is UIKit; SwiftUI `CloudSharingView` availability varies by OS — check docs for your SDK and fall back if needed.",
        ],
        "Xcode iOS app",
        [("CKShare", "https://developer.apple.com/documentation/cloudkit/ckshare"),
         ("Get the most out of CloudKit Sharing", "https://developer.apple.com/videos/play/tech-talks/10874/")],
    ))


def project_16():
    d = ROOT / "16-architecture-testing"
    name = "ArchitectureTesting"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "ArchitectureTesting.swift", f'''\
import Foundation

public struct TodoItem: Identifiable, Equatable, Sendable {{
    public let id: UUID
    public var title: String
    public var isDone: Bool
    public init(id: UUID = UUID(), title: String, isDone: Bool = false) {{
        self.id = id; self.title = title; self.isDone = isDone
    }}
}}

public protocol TodoRepository: Sendable {{
    func all() async -> [TodoItem]
    func save(_ item: TodoItem) async
}}

public actor InMemoryTodoRepository: TodoRepository {{
    private var items: [TodoItem] = []
    public init() {{}}
    public func all() async -> [TodoItem] {{ items }}
    public func save(_ item: TodoItem) async {{
        if let idx = items.firstIndex(where: {{ $0.id == item.id }}) {{ items[idx] = item }}
        else {{ items.append(item) }}
    }}
}}

public final class TodoViewModel: @unchecked Sendable {{
    private let repository: any TodoRepository
    public private(set) var items: [TodoItem] = []

    public init(repository: any TodoRepository) {{
        self.repository = repository
    }}

{todo_block(
    "MVVM + Swift Testing",
    "Load/add/toggle todos through the view model; test behavior without UI.",
    [
        "Implement `refresh()`, `add(title:)`, `toggle(id:)`.",
        "Keep transformation logic in the view model / repository — not in SwiftUI views.",
        "Write `#expect` / `#require` tests in the test target.",
    ],
    ["Swift Testing ships with the toolchain — `import Testing`.",
     "https://developer.apple.com/documentation/testing"],
    ["Tests cover add + toggle without flaking."],
    [
        "https://developer.apple.com/documentation/testing",
        "https://docs.swift.org/latest/documentation/testing/expectations/",
        "https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app",
    ],
)}
    // public func refresh() async {{ fatalError("TODO") }}
    // public func add(title: String) async {{ fatalError("TODO") }}
    // public func toggle(id: UUID) async {{ fatalError("TODO") }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", "import ArchitectureTesting\nprint(\"Run swift test after implementing ViewModel TODOs\")\n")
    write(d / "Tests" / f"{name}Tests" / "ArchitectureTestingTests.swift", '''\
import Testing
@testable import ArchitectureTesting

@Test func repositoryStartsEmpty() async {
    let repo = InMemoryTodoRepository()
    #expect(await repo.all().isEmpty)
}

// @Test @MainActor func addAndToggle() async {
//     let vm = TodoViewModel(repository: InMemoryTodoRepository())
//     await vm.add(title: "Ship course")
//     #expect(vm.items.count == 1)
// }
''')
    write(d / "README.md", readme_project(
        "16", "Architecture (MVVM) + Swift Testing",
        ["MVVM boundaries", "Repository pattern", "Swift Testing (#expect/#require)", "@MainActor view models"],
        "A testable todo domain + view model (UI optional in Xcode later).",
        ["Implement VM methods", "Uncomment/add tests", "`swift test`"],
        ["Add a SwiftUI thin view layer in an Xcode app that only renders VM state"],
        "Xcode 16+ / Swift 6; Linux `swift test` OK for domain layer.",
        [],
        "Swift Package",
        [("Swift Testing", "https://developer.apple.com/documentation/testing"),
         ("Expectations", "https://docs.swift.org/latest/documentation/testing/expectations/")],
    ))


def main() -> None:
    print("Generating 06-16...")
    for fn in [
        project_06, project_07, project_08, project_09, project_10, project_11,
        project_12, project_13, project_14, project_15, project_16,
    ]:
        fn()
    print("06-16 done")


if __name__ == "__main__":
    main()
