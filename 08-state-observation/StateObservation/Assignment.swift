import Observation

@Observable
final class CounterModel {
    var count: Int = 0
    // TODO: add reset() and increment(by:)
}
// MARK: - TODO: Observation & bindings
/*
 Goal:
 Drive the UI from an @Observable model and two-way bindings.

 Steps:
 1. Hold `@State private var model = CounterModel()` in ContentView.
 2. Show count, buttons to increment/reset.
 3. Add a Toggle bound to a `isHighlighted` Bool on the model (add the property).
 4. Remember: @State for Observable classes is lazily initialized on newer SDKs (WWDC26 / back-deployed).

 Hints:
 - Prefer @Observable over ObservableObject for new code.
 - Use Bindable(model) when you need bindings to observable properties.

 Acceptance criteria:
 - UI updates when count changes without manual objectWillChange.

 Docs:
 - https://developer.apple.com/documentation/observation
 - https://developer.apple.com/documentation/observation/observable()
 - https://developer.apple.com/documentation/swiftui/bindable
 - https://developer.apple.com/videos/play/wwdc2026/269/
*/
