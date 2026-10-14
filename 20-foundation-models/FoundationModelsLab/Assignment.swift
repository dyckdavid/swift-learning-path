// MARK: - TODO: On-device language model session
/*
 Goal:
 Use the Foundation Models framework to summarize text on-device.

 Steps:
 1. `import FoundationModels`
 2. Create a `LanguageModelSession` (optionally with instructions / tools).
 3. Call `respond` (or streaming `streamResponse`) with a user prompt.
 4. Define a `@Generable` struct (e.g. title + bullet points) and request typed output.
 5. Gate on Apple Intelligence availability / supported devices.

 Hints:
 - Framework docs: https://developer.apple.com/documentation/foundationmodels
 - WWDC25 intro: https://developer.apple.com/videos/play/wwdc2025/286/
 - WWDC25 deep dive: https://developer.apple.com/videos/play/wwdc2025/301/
 - Newer SDKs also discuss Private Cloud Compute models and `LanguageModel` providers — only use APIs listed in your installed SDK’s doc archive.

 Acceptance criteria:
 - Given a long paragraph, app shows a structured summary without a custom server.

 Docs:
 - https://developer.apple.com/documentation/foundationmodels
 - https://developer.apple.com/documentation/foundationmodels/languagemodelsession
 - https://developer.apple.com/foundation-models-framework/
 - https://developer.apple.com/videos/play/wwdc2025/286/
*/

/*
 Verified API names from Apple documentation (use autocomplete in Xcode 27 to confirm signatures):
 - import FoundationModels
 - LanguageModelSession
 - SystemLanguageModel / PrivateCloudComputeLanguageModel (availability varies)
 - @Generable / @Guide
 - Tool protocol for tool calling
 - session.respond / streamResponse

 If an initializer or type is missing in your SDK, do NOT invent it — check the doc page for your SDK
 and note the discrepancy in a comment.
*/
