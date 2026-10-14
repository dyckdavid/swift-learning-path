# 05. Concurrency — async/await, Actors, Swift 6

## Concepts
- async/await
- actors & isolation
- Task / TaskGroup
- Swift 6 strict concurrency / Sendable

## What you’ll build
An actor-backed scoreboard and a concurrent fan-out loader.

## Project type
Swift Package (Swift 6)

## Steps overview
1. Implement actor increment
2. Implement TaskGroup loader
3. Enable complete concurrency checking in Xcode if needed

## Stretch goals
- Add `AsyncSequence` ticker
- Experiment with `@MainActor` UI boundary types (preview for SwiftUI projects)

## Required tooling
Xcode 16+ with Swift 6 language mode; Linux `swift test` OK for this package.

## Docs (verify APIs here)
- [Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)
- [Swift 6 concurrency migration guide](https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/)
- [actor](https://developer.apple.com/documentation/swift/actor)

## Untested / Apple-only notes
- UIKit/SwiftUI main-actor UI not covered here.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
