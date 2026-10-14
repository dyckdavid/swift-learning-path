# 28. watchOS Companion

## Concepts
- watchOS SwiftUI lifecycle
- Shared model via App Group / WatchConnectivity
- Complications (optional)

## What you’ll build
A watchOS timer companion that mirrors a simple iOS host counter.

## Project type
Xcode iOS host + (you add) watchOS app target

## Steps overview
1. On Mac with Xcode: File → New → Project → iOS App + watchOS App (or add Watch App target to the provided host).
2. Implement a shared Int counter using App Groups UserDefaults **or** WatchConnectivity.
3. Show the value on both iOS and watchOS UIs.
4. Optional: circular complication.

## Stretch goals
- Independent watchOS app (no phone) variant

## Required tooling
Xcode 27 with watchOS SDK; hardware Watch optional (simulator OK).

## Docs (verify APIs here)
- [watchOS apps](https://developer.apple.com/documentation/watchos-apps)
- [Watch Connectivity](https://developer.apple.com/documentation/watchconnectivity)
- [SwiftUI on watchOS](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps/)

## Untested / Apple-only notes
- Full dual-target project generation is brittle without Xcode — this folder ships an **iOS host scaffold** plus instructions to add the Watch target.
- Apple-only; untested here.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
