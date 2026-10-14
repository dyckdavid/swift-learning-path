# 29. Latest OS APIs & Liquid Glass

## Concepts
- Liquid Glass (glassEffect / glass button styles)
- Toolbar overflow & visibilityPriority
- iOS 27 resizability
- Prominent tabs

## What you’ll build
A small showcase app for modern system design + WWDC26 SwiftUI additions.

## Project type
Xcode iOS app

## Steps overview
1. Build with iOS 27 SDK
2. Implement glass + toolbar TODOs
3. Resize preview / mirroring test

## Stretch goals
- Document APIs from WWDC26 session 269 (AsyncImage caching, ContentBuilder notes)
- Explore new Document protocols if you extend into documents

## Required tooling
**Xcode 27** + iOS 27 SDK (deployment 26+ for glass APIs).

## Docs (verify APIs here)
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
- [glassEffect](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:))
- [What’s new in SwiftUI — WWDC26](https://developer.apple.com/videos/play/wwdc2026/269/)

## Untested / Apple-only notes
- Not compile-verified here.
- Some WWDC26 toolbar symbol names (`ToolbarOverflowMenu`, `visibilityPriority`, `topBarPinnedTrailing`) are taken from Apple’s WWDC26 session transcript — confirm exact spellings/availability in your installed SDK documentation before shipping.
- Liquid Glass overview: https://developer.apple.com/documentation/technologyoverviews/liquid-glass

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
