# 17. App Architecture at Scale — Modular Packages

## Concepts
- Swift Package modularization
- Feature modules vs core
- Dependency direction
- Local package product linking

## What you’ll build
A small modular workspace: `Core`, `FeatureTodos`, and `AppShell` executable that depends on features.

## Project type
Multi-package SwiftPM workspace

## Steps overview
1. Explore the three packages under this folder
2. Keep Feature → Core dependencies only (no Feature ↔ Feature cycles)
3. Implement the TODO in FeatureTodos that uses Core models
4. Build with `swift build` from AppShell

## Stretch goals
- Add a FeatureSettings package
- Introduce a public protocol in Core for analytics

## Required tooling
Xcode 16+ / Swift 6; Linux `swift build` OK for packages.

## Docs (verify APIs here)
- [Organizing your code with Swift packages](https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages)
- [SwiftPM](https://docs.swift.org/package-manager/)

## Untested / Apple-only notes
- iOS UI shell is package-based here; shipping App Store apps still need an Xcode app target that links local packages.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
