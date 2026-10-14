# 18. Widgets & Live Activities

## Concepts
- WidgetKit timelines
- ActivityKit
- Dynamic Island presentations
- App Groups (optional)

## What you’ll build
Focus timer widget + Live Activity.

## Project type
Xcode iOS app + (you add) Widget Extension

## Steps overview
1. Add Widget Extension target in Xcode
2. Implement timeline + ActivityConfiguration
3. Start/update/end from app

## Stretch goals
- ActivityKit push updates
- Interactive widget buttons

## Required tooling
Xcode 27 / iOS 17+ (Live Activities); physical device recommended for Dynamic Island.

## Docs (verify APIs here)
- [WidgetKit](https://developer.apple.com/documentation/widgetkit)
- [ActivityKit](https://developer.apple.com/documentation/activitykit)
- [Live Activities essentials — WWDC26](https://developer.apple.com/videos/play/wwdc2026/223/)

## Untested / Apple-only notes
- Extension target cannot be fully authored without Xcode — placeholder documented.
- ActivityKit/WidgetKit Apple-only; not buildable on Linux.
- iOS 27 landscape Dynamic Island style covered in WWDC26 session 223 — adopt when available in your SDK.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
