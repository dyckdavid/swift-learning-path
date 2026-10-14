// MARK: - TODO: VoiceOver & Dynamic Type
/*
 Goal:
 Make a custom control accessible and respect Dynamic Type.

 Steps:
 1. Replace a tappable RoundedRectangle with a real Button (or add accessibility traits/actions).
 2. Add `.accessibilityLabel` / `.accessibilityHint` / `.accessibilityValue` as needed.
 3. Use scalable fonts (`.font(.body)` etc.) and test with larger content sizes.
 4. Verify with Accessibility Inspector / VoiceOver on device.

 Hints:
 - Prefer native controls — they inherit accessibility.
 - Combine elements with `accessibilityElement(children: .combine)` when appropriate.

 Acceptance criteria:
 - VoiceOver reads meaningful labels; UI remains usable at XXXL content size.

 Docs:
 - https://developer.apple.com/documentation/swiftui/view/accessibilitylabel(_:)
 - https://developer.apple.com/documentation/accessibility
 - https://developer.apple.com/accessibility/xcode/
*/
