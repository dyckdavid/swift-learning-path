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
// MARK: - TODO: Widget timeline + Live Activity
/*
 Goal:
 Ship a home-screen widget and a Live Activity for a focus timer.

 Steps:
 1. In Xcode: add a Widget Extension; enable Live Activities in Info.plist (`NSSupportsLiveActivities`).
 2. Implement a `TimelineProvider` + `View` for `.systemSmall` (and optionally `.systemExtraLargePortrait` on iOS 27).
 3. Implement `ActivityConfiguration` for `FocusAttributes` (Lock Screen + Dynamic Island).
 4. From the app, `Activity.request` / `update` / `end` using ActivityKit.

 Hints:
 - WWDC26: Live Activities essentials — https://developer.apple.com/videos/play/wwdc2026/223/
 - WWDC26: WidgetKit foundations — https://developer.apple.com/videos/play/wwdc2026/277/

 Acceptance criteria:
 - Widget renders glanceable state; Live Activity updates while timer runs.

 Docs:
 - https://developer.apple.com/documentation/widgetkit
 - https://developer.apple.com/documentation/activitykit
 - https://developer.apple.com/documentation/activitykit/activity
 - https://developer.apple.com/videos/play/wwdc2026/223/
 - https://developer.apple.com/videos/play/wwdc2026/277/
*/
