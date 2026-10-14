# 20. Apple Intelligence — Foundation Models

## Concepts
- LanguageModelSession
- @Generable guided generation
- Tool calling (optional)
- Availability / device support

## What you’ll build
On-device text summarizer with structured output.

## Project type
Xcode iOS app

## Steps overview
1. Import FoundationModels
2. Implement session + Generable summary
3. Handle unsupported devices gracefully

## Stretch goals
- Add a Tool that fetches local notes
- Try streaming tokens into the UI

## Required tooling
**Xcode 27** + Apple Intelligence–capable Mac/iPhone. Deployment target set to iOS 26+ in project (adjust if your SDK expects 27).

## Docs (verify APIs here)
- [Foundation Models](https://developer.apple.com/documentation/foundationmodels)
- [LanguageModelSession](https://developer.apple.com/documentation/foundationmodels/languagemodelsession)
- [Meet the Foundation Models framework — WWDC25](https://developer.apple.com/videos/play/wwdc2025/286/)

## Untested / Apple-only notes
- Cannot compile/verify Foundation Models on Linux.
- Exact initializer signatures evolve — confirm in Xcode’s SDK docs; cited types are from Apple’s Foundation Models documentation.
- Private Cloud Compute / third-party LanguageModel providers: use only if present in your SDK docs.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
