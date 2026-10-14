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
// MARK: - TODO: App Intent + App Shortcut
/*
 Goal:
 Expose a parameterised intent to Shortcuts / Siri / Spotlight.

 Steps:
 1. Add an `@Parameter` (e.g. minutes: Int) to an intent.
 2. Return a dialog or opensIntent result as appropriate.
 3. Implement `AppShortcutsProvider` with phrases using `\(.applicationName)`.
 4. Run from Shortcuts app and via Siri phrase.

 Hints:
 - Keep intents focused on core user actions.
 - https://developer.apple.com/documentation/appintents/appintent

 Acceptance criteria:
 - Intent appears in Shortcuts; App Shortcut phrase invokes it.

 Docs:
 - https://developer.apple.com/documentation/appintents
 - https://developer.apple.com/documentation/appintents/appintent
 - https://developer.apple.com/documentation/appintents/appshortcutsprovider
 - https://developer.apple.com/videos/play/wwdc2025/244/
*/
