# 27. macOS App

## Concepts
- NavigationSplitView
- Settings scene
- Commands / shortcuts
- macOS windowing

## What you’ll build
A multi-pane Mac notes shell.

## Project type
Xcode macOS app (verify destination on open)

## Steps overview
1. Open in Xcode as a Mac run destination
2. Implement split view + settings + ⌘N

## Stretch goals
- Menu bar extra
- DocumentGroup / new Document APIs from WWDC26

## Required tooling
Xcode 27 / macOS 27 SDK recommended (deployment 14+ OK for basics).

## Docs (verify APIs here)
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview)
- [Settings](https://developer.apple.com/documentation/swiftui/settings)

## Untested / Apple-only notes
- Committed pbxproj may still list iOS SDK defaults in some build settings — set the run destination to My Mac and fix TARGETED_DEVICE_FAMILY / SDKROOT in Xcode if needed (or regenerate with XcodeGen and macOS platform).
- Not buildable on Linux.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
