// MARK: - TODO: String Catalog localization
/*
 Goal:
 Localize UI strings with a String Catalog and exercise plurals.

 Steps:
 1. Enable `SWIFT_EMIT_LOC_STRINGS` (already on in project settings).
 2. Add `Localizable.xcstrings` (String Catalog) via Xcode.
 3. Replace hardcoded strings with `String(localized:)` / LocalizedStringResource / Text("key").
 4. Add at least one plural variation (e.g. "%lld tasks left").
 5. Add a second language (e.g. Spanish) and switch device language to verify.

 Hints:
 - String Catalogs are the modern replacement for sprawling Localizable.strings workflows.
 - https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog

 Acceptance criteria:
 - UI shows translated strings; plurals correct for 0/1/many.

 Docs:
 - https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog
 - https://developer.apple.com/documentation/foundation/string/init(localized:)
*/
