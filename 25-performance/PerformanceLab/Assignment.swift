// MARK: - TODO: Find and fix a hitch
/*
 Goal:
 Use Instruments to diagnose a deliberately inefficient SwiftUI screen, then fix it.

 Steps:
 1. Build a List of 5_000 items with an intentionally expensive row (e.g. heavy synchronous work in `body`).
 2. Profile with Instruments → SwiftUI / Time Profiler / Hitches (Xcode 27 Instruments workflows).
 3. Move work off the hot path (precompute, cache, simplify view body, use `EquatableView` patterns carefully).
 4. Write a short PERF_NOTES.md: before/after + screenshot names.

 Hints:
 - Prefer fixing algorithmic work before micro-optimizing.
 - WWDC26 Xcode/Instruments sessions discuss responsiveness tooling.

 Acceptance criteria:
 - Scrolling remains responsive after fix; notes document the measurement.

 Docs:
 - https://developer.apple.com/documentation/xcode/improving-your-app-s-performance
 - https://developer.apple.com/videos/play/wwdc2026/258/
 - https://developer.apple.com/documentation/swiftui/view-performance
*/
