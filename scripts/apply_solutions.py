#!/usr/bin/env python3
"""Apply reference solutions onto the current working tree (for solutions branch)."""

from pathlib import Path

ROOT = Path("/workspace")


def w(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")


def main() -> None:
    # 01
    w("01-swift-basics/Sources/SwiftBasics/SwiftBasics.swift", '''\
/// Project 01 — solutions
public enum TemperatureUnit: String, Sendable {
    case celsius
    case fahrenheit
}

public struct MeasurementSample: Equatable, Sendable {
    public var value: Double
    public var unit: TemperatureUnit
    public init(value: Double, unit: TemperatureUnit) {
        self.value = value
        self.unit = unit
    }
}

public enum BasicsExercises {
    public static func greet(name: String) -> String { "Hello, \\(name)!" }

    public static func parseScore(_ text: String, default defaultValue: Int) -> Int {
        Int(text) ?? defaultValue
    }

    public static func wordFrequencies(in words: [String]) -> [String: Int] {
        var result: [String: Int] = [:]
        for word in words {
            let key = word.trimmingCharacters(in: .whitespacesAndNewlines).lowercased()
            guard !key.isEmpty else { continue }
            result[key, default: 0] += 1
        }
        return result
    }

    public static func converted(_ sample: MeasurementSample, to unit: TemperatureUnit) -> MeasurementSample {
        guard sample.unit != unit else { return sample }
        switch (sample.unit, unit) {
        case (.celsius, .fahrenheit):
            return MeasurementSample(value: sample.value * 9 / 5 + 32, unit: .fahrenheit)
        case (.fahrenheit, .celsius):
            return MeasurementSample(value: (sample.value - 32) * 5 / 9, unit: .celsius)
        default:
            return sample
        }
    }
}
''')
    w("01-swift-basics/Tests/SwiftBasicsTests/SwiftBasicsTests.swift", '''\
import Testing
@testable import SwiftBasics

@Test func greetWorks() {
    #expect(BasicsExercises.greet(name: "David") == "Hello, David!")
}

@Test func parseScore() {
    #expect(BasicsExercises.parseScore("42", default: 0) == 42)
    #expect(BasicsExercises.parseScore("nope", default: 7) == 7)
}

@Test func frequencies() {
    #expect(BasicsExercises.wordFrequencies(in: ["Hi", "hi", " ", "Yo"]) == ["hi": 2, "yo": 1])
}

@Test func temperature() {
    let c = MeasurementSample(value: 0, unit: .celsius)
    #expect(BasicsExercises.converted(c, to: .fahrenheit).value == 32)
}
''')

    # 02
    w("02-functions-closures/Sources/FunctionsClosures/FunctionsClosures.swift", '''\
public enum MathOps {
    public static func identity(_ value: Int) -> Int { value }

    public static func squaredEvens(in values: [Int]) -> [Int] {
        values.filter { $0.isMultiple(of: 2) }.map { $0 * $0 }
    }

    public static func sum(of values: [Int], using combine: (Int, Int) -> Int) -> Int {
        values.reduce(0, combine)
    }

    nonisolated(unsafe) public static var shouldSucceed: Bool = true

    public static func perform(success: (String) -> String, failure: () -> String) -> String {
        shouldSucceed ? success("ok") : failure()
    }
}
''')

    # 03
    w("03-types-and-oop/Sources/TypesAndOOP/TypesAndOOP.swift", '''\
public struct Point: Equatable, Sendable {
    public var x: Double
    public var y: Double
    public init(x: Double, y: Double) { self.x = x; self.y = y }
}

public enum Shape: Equatable, Sendable {
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
}

public final class Counter: @unchecked Sendable {
    public private(set) var value: Int
    public init(value: Int = 0) { self.value = value }
    public func increment() { value += 1 }
}

public enum TypeExercises {
    public static func area(of shape: Shape) -> Double {
        switch shape {
        case .circle(let r): return Double.pi * r * r
        case .rectangle(let w, let h): return w * h
        }
    }

    public static func moved(_ point: Point, by delta: Point) -> Point {
        Point(x: point.x + delta.x, y: point.y + delta.y)
    }

    public static func bumpTwice(_ counter: Counter) -> Int {
        counter.increment(); counter.increment(); return counter.value
    }
}
''')

    # 04
    w("04-protocols-generics-errors/Sources/ProtocolsGenerics/ProtocolsGenerics.swift", '''\
public protocol IdentifiableItem: Sendable {
    var id: String { get }
}

public struct User: IdentifiableItem, Equatable, Sendable {
    public let id: String
    public var name: String
    public init(id: String, name: String) { self.id = id; self.name = name }
}

public enum StoreError: Error, Equatable, Sendable {
    case notFound(id: String)
    case emptyName
}

public struct MemoryStore<Item: IdentifiableItem>: Sendable {
    private var items: [String: Item]
    public init(items: [Item] = []) {
        self.items = Dictionary(uniqueKeysWithValues: items.map { ($0.id, $0) })
    }

    public func all() -> [Item] { Array(items.values) }

    public func item(id: String) throws -> Item {
        guard let item = items[id] else { throw StoreError.notFound(id: id) }
        return item
    }

    public mutating func upsert(_ item: Item) {
        items[item.id] = item
    }
}

public func validatedName(_ raw: String) throws -> String {
    let trimmed = raw.trimmingCharacters(in: .whitespacesAndNewlines)
    guard !trimmed.isEmpty else { throw StoreError.emptyName }
    return trimmed
}
''')

    # 05
    w("05-concurrency/Sources/ConcurrencyLab/ConcurrencyLab.swift", '''\
public actor ScoreBoard: Sendable {
    private var scores: [String: Int] = [:]
    public init() {}

    public func setScore(_ score: Int, for player: String) { scores[player] = score }
    public func score(for player: String) -> Int? { scores[player] }

    public func addPoints(_ points: Int, to player: String) {
        scores[player, default: 0] += points
    }
}

public enum AsyncExercises {
    public static func fakeFetch(id: String) async -> (id: String, value: Int) {
        try? await Task.sleep(for: .milliseconds(10))
        return (id, id.count)
    }

    public static func loadAll(ids: [String]) async -> [(id: String, value: Int)] {
        await withTaskGroup(of: (id: String, value: Int).self) { group in
            for id in ids {
                group.addTask { await fakeFetch(id: id) }
            }
            var results: [(id: String, value: Int)] = []
            for await item in group { results.append(item) }
            return results.sorted { $0.id < $1.id }
        }
    }
}
''')

    # 11
    w("11-networking-codable/Sources/NetworkingCodable/NetworkingCodable.swift", '''\
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

public struct RemotePost: Codable, Equatable, Sendable, Identifiable {
    public let id: Int
    public let title: String
    public let body: String
}

public protocol HTTPSession: Sendable {
    func data(for request: URLRequest) async throws -> (Data, URLResponse)
}

extension URLSession: HTTPSession {
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {
        #if canImport(FoundationNetworking)
        try await withCheckedThrowingContinuation { (cont: CheckedContinuation<(Data, URLResponse), Error>) in
            let task = self.dataTask(with: request) { data, response, error in
                if let error { cont.resume(throwing: error) }
                else if let data, let response { cont.resume(returning: (data, response)) }
                else { cont.resume(throwing: URLError(.badServerResponse)) }
            }
            task.resume()
        }
        #else
        try await self.data(for: request)
        #endif
    }
}

public struct PostClient: Sendable {
    private let session: any HTTPSession
    private let baseURL: URL

    public init(session: any HTTPSession = URLSession.shared, baseURL: URL = URL(string: "https://jsonplaceholder.typicode.com")!) {
        self.session = session
        self.baseURL = baseURL
    }

    public func fetchPosts() async throws -> [RemotePost] {
        let url = baseURL.appendingPathComponent("posts")
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse, (200..<300).contains(http.statusCode) else {
            throw URLError(.badServerResponse)
        }
        return try JSONDecoder().decode([RemotePost].self, from: data)
    }
}

public struct FixtureSession: HTTPSession, Sendable {
    public var data: Data
    public var statusCode: Int
    public init(data: Data, statusCode: Int = 200) {
        self.data = data
        self.statusCode = statusCode
    }
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {
        let response = HTTPURLResponse(url: request.url!, statusCode: statusCode, httpVersion: nil, headerFields: nil)!
        return (data, response)
    }
}
''')
    w("11-networking-codable/Tests/NetworkingCodableTests/NetworkingCodableTests.swift", '''\
import Foundation
import Testing
@testable import NetworkingCodable

@Test func fixtureRoundTrip() throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let posts = try JSONDecoder().decode([RemotePost].self, from: json)
    #expect(posts.first?.id == 1)
}

@Test func fetchPostsUsesFixture() async throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let client = PostClient(session: FixtureSession(data: json))
    let posts = try await client.fetchPosts()
    #expect(posts.count == 1)
}
''')

    # 16
    w("16-architecture-testing/Sources/ArchitectureTesting/ArchitectureTesting.swift", '''\
import Foundation

public struct TodoItem: Identifiable, Equatable, Sendable {
    public let id: UUID
    public var title: String
    public var isDone: Bool
    public init(id: UUID = UUID(), title: String, isDone: Bool = false) {
        self.id = id; self.title = title; self.isDone = isDone
    }
}

public protocol TodoRepository: Sendable {
    func all() async -> [TodoItem]
    func save(_ item: TodoItem) async
}

public actor InMemoryTodoRepository: TodoRepository {
    private var items: [TodoItem] = []
    public init() {}
    public func all() async -> [TodoItem] { items }
    public func save(_ item: TodoItem) async {
        if let idx = items.firstIndex(where: { $0.id == item.id }) { items[idx] = item }
        else { items.append(item) }
    }
}

public final class TodoViewModel: @unchecked Sendable {
    private let repository: any TodoRepository
    public private(set) var items: [TodoItem] = []

    public init(repository: any TodoRepository) {
        self.repository = repository
    }

    public func refresh() async {
        items = await repository.all()
    }

    public func add(title: String) async {
        let item = TodoItem(title: title)
        await repository.save(item)
        await refresh()
    }

    public func toggle(id: UUID) async {
        guard var item = items.first(where: { $0.id == id }) else { return }
        item.isDone.toggle()
        await repository.save(item)
        await refresh()
    }
}
''')
    w("16-architecture-testing/Tests/ArchitectureTestingTests/ArchitectureTestingTests.swift", '''\
import Testing
@testable import ArchitectureTesting

@Test func repositoryStartsEmpty() async {
    let repo = InMemoryTodoRepository()
    #expect(await repo.all().isEmpty)
}

@Test func addAndToggle() async {
    let vm = TodoViewModel(repository: InMemoryTodoRepository())
    await vm.add(title: "Ship course")
    #expect(vm.items.count == 1)
    let id = vm.items[0].id
    await vm.toggle(id: id)
    #expect(vm.items[0].isDone)
}
''')

    # 17
    w("17-modularization/Sources/FeatureTodos/FeatureTodos.swift", '''\
import Core

public enum TodoFeature {
    public static func sample() -> [TodoDTO] {
        [TodoDTO(title: "Learn modules")]
    }

    public static func openTodos(in items: [TodoDTO]) -> [TodoDTO] {
        items.filter { !$0.title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty }
    }
}
''')

    # 26 macro expansion
    w("26-swift-macros/Sources/SwiftMacrosLabMacros/SwiftMacrosLabMacros.swift", '''\
import SwiftCompilerPlugin
import SwiftSyntax
import SwiftSyntaxBuilder
import SwiftSyntaxMacros

public struct StringifyMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) throws -> ExprSyntax {
        guard let argument = node.arguments.first?.expression else {
            throw MacroError.message("stringify(_:) requires an argument")
        }
        return "(\(argument), \\(literal: argument.description))"
    }
}

enum MacroError: Error, CustomStringConvertible {
    case message(String)
    var description: String {
        switch self {
        case .message(let text): return text
        }
    }
}

@main
struct SwiftMacrosLabPlugin: CompilerPlugin {
    let providingMacros: [Macro.Type] = [StringifyMacro.self]
}
''')

    # App project solutions — ContentView / Assignment implementations
    solutions_apps = {
        "06-swiftui-basics": ("SwiftUIBasics", '''\
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Image(systemName: "person.circle.fill")
                    .font(.system(size: 72))
                    .foregroundStyle(.tint)
                Text("David")
                    .font(.title.bold())
                Text("Learning Swift from fundamentals to pro-level apps.")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                Spacer()
            }
            .padding()
            .navigationTitle("Basics")
        }
    }
}

#Preview { ContentView() }
'''),
        "08-state-observation": ("StateObservation", '''\
import SwiftUI
import Observation

@Observable
final class CounterModel {
    var count: Int = 0
    var isHighlighted: Bool = false
    func increment(by amount: Int = 1) { count += amount }
    func reset() { count = 0 }
}

struct ContentView: View {
    @State private var model = CounterModel()

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                Text("\\(model.count)")
                    .font(.largeTitle.bold())
                    .foregroundStyle(model.isHighlighted ? .orange : .primary)
                HStack {
                    Button("−") { model.increment(by: -1) }
                    Button("+") { model.increment() }
                    Button("Reset") { model.reset() }
                }
                .buttonStyle(.borderedProminent)
                Toggle("Highlight", isOn: Bindable(model).isHighlighted)
            }
            .padding()
            .navigationTitle("Counter")
        }
    }
}

#Preview { ContentView() }
'''),
        "11-skip": None,
    }

    for folder, payload in solutions_apps.items():
        if payload is None:
            continue
        name, content = payload
        w(f"{folder}/{name}/ContentView.swift", content)
        # Remove Assignment.swift TODOs where ContentView absorbed them
        assign = ROOT / folder / name / "Assignment.swift"
        if assign.exists() and folder in {"06-swiftui-basics", "08-state-observation"}:
            assign.unlink()

    # Generic richer Assignment solutions for remaining apps
    app_assignments = {
        "07-navigation-lists/NavigationLists/Assignment.swift": '''\
import SwiftUI

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

struct LibraryRoot: View {
    @State private var items = SampleData.items
    var body: some View {
        List {
            ForEach(items) { item in
                NavigationLink(value: item) { Text(item.title) }
            }
            .onDelete { items.remove(atOffsets: $0) }
        }
        .navigationDestination(for: SampleItem.self) { item in
            Text(item.title).font(.largeTitle)
        }
        .toolbar { EditButton() }
    }
}
''',
        "09-forms/FormsLab/Assignment.swift": '''\
import SwiftUI

struct ProfileForm: View {
    @State private var name = ""
    @State private var difficulty = 1
    @State private var notifications = true
    @State private var showAlert = false

    private var canSave: Bool {
        !name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }

    var body: some View {
        Form {
            Section("Profile") {
                TextField("Display name", text: $name)
                Picker("Difficulty", selection: $difficulty) {
                    Text("Easy").tag(0)
                    Text("Normal").tag(1)
                    Text("Hard").tag(2)
                }
                Toggle("Notifications", isOn: $notifications)
            }
            Button("Save") { showAlert = true }
                .disabled(!canSave)
        }
        .alert("Saved", isPresented: $showAlert) {
            Button("OK", role: .cancel) {}
        } message: {
            Text("\\(name) · difficulty \\(difficulty) · notifications \\(notifications)")
        }
    }
}
''',
        "12-swiftdata/SwiftDataLab/Assignment.swift": '''\
import Foundation
import SwiftData

@Model
final class Note {
    var title: String
    var createdAt: Date
    init(title: String, createdAt: Date = .now) {
        self.title = title
        self.createdAt = createdAt
    }
}
''',
        "17-modularization/Sources/FeatureTodos/FeatureTodos.swift": '''\
import Core

public enum TodoFeature {
    public static func sample() -> [TodoDTO] {
        [TodoDTO(title: "Learn modules")]
    }

    public static func openTodos(in items: [TodoDTO]) -> [TodoDTO] {
        items.filter { !$0.title.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty }
    }
}
''',
    }
    for rel, content in app_assignments.items():
        w(rel, content)

    # Patch a few App entry points for SwiftData solutions
    w("12-swiftdata/SwiftDataLab/SwiftDataLabApp.swift", '''\
import SwiftUI
import SwiftData

@main
struct SwiftDataLabApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: Note.self)
    }
}
''')
    w("12-swiftdata/SwiftDataLab/ContentView.swift", '''\
import SwiftUI
import SwiftData

struct ContentView: View {
    @Environment(\\.modelContext) private var context
    @Query(sort: \\Note.createdAt, order: .reverse) private var notes: [Note]
    var body: some View {
        NavigationStack {
            List {
                ForEach(notes) { note in
                    Text(note.title)
                }
                .onDelete { indexSet in
                    for index in indexSet { context.delete(notes[index]) }
                }
            }
            .navigationTitle("Notes")
            .toolbar {
                Button("Add") {
                    context.insert(Note(title: "Note \\(notes.count + 1)"))
                }
            }
        }
    }
}
''')

    # 07 ContentView uses LibraryRoot
    w("07-navigation-lists/NavigationLists/ContentView.swift", '''\
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            LibraryRoot()
                .navigationTitle("Library")
        }
    }
}

#Preview { ContentView() }
''')

    w("09-forms/FormsLab/ContentView.swift", '''\
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            ProfileForm()
                .navigationTitle("Profile")
        }
    }
}

#Preview { ContentView() }
''')

    # Solutions note
    w("SOLUTIONS.md", '''\
# Solutions branch

This branch contains reference implementations for the Swift Learning Path assignments.

- Prefer completing work on `main` first.
- Treat these solutions as one valid approach, not the only approach.
- Apple-framework projects (SwiftUI, CloudKit, etc.) are still **not compile-verified** in Linux CI; open them in Xcode 27 on a Mac.
''')

    print("Solutions applied")


if __name__ == "__main__":
    main()
