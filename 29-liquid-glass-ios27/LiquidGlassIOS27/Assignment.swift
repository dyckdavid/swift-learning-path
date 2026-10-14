// MARK: - TODO: Adopt Liquid Glass + iOS 27 SwiftUI APIs
/*
 Goal:
 Build a resizable, glass-polished starter that uses verified iOS 26/27 APIs.

 Steps:
 1. Apply `.glassEffect(_:in:)` to a custom control; prefer `.buttonStyle(.glass)` for buttons.
 2. Group related glass views in `GlassEffectContainer` when using multiple effects.
 3. Try toolbar APIs from WWDC26: `visibilityPriority`, `ToolbarOverflowMenu`, `toolbarMinimizeBehavior`.
 4. Exercise resizability (iPhone apps are resizable in iOS 27 — test with Live Preview resize handles / iPhone Mirroring).
 5. Optional: `Tab(role: .prominent)` for a distinct tab.

 Hints:
 - Liquid Glass landed broadly with iOS 26; iOS 27 refreshes it further — standard components adopt automatically when building with latest SDK.
 - Do not invent glass APIs; confirm `.glassEffect` in your SDK docs.

 Acceptance criteria:
 - UI shows glass styling; toolbar behavior remains usable when the window is narrow.

 Docs:
 - https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass
 - https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)
 - https://developer.apple.com/documentation/technologyoverviews/liquid-glass
 - https://developer.apple.com/videos/play/wwdc2026/269/
 - https://developer.apple.com/videos/play/wwdc2026/278/
*/

/*
 Example shapes (verify in SDK):
   Text("Hello")
     .padding()
     .glassEffect(.regular, in: .rect(cornerRadius: 16))

 Gate if you support older OS:
   if #available(iOS 26, *) { ... } else { ... material fallback ... }
*/
