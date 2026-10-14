import AppIntents

struct OpenStudyIntent: AppIntent {
    static var title: LocalizedStringResource = "Open Study Session"
    static var description = IntentDescription("Starts a timed study session.")

    @Parameter(title: "Minutes")
    var minutes: Int

    static var parameterSummary: some ParameterSummary {
        Summary("Study for \(\.$minutes) minutes")
    }

    func perform() async throws -> some IntentResult & ProvidesDialog {
        .result(dialog: "Starting a \(minutes)-minute study session.")
    }
}

struct StudyShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: OpenStudyIntent(),
            phrases: [
                "Start studying in \(.applicationName)",
                "Study session in \(.applicationName)"
            ],
            shortTitle: "Study",
            systemImageName: "book.fill"
        )
    }
}
