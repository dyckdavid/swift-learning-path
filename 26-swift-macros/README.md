# 26. Swift Macros & Authoring Packages

## Concepts
- Freestanding macros
- CompilerPlugin
- SwiftSyntax
- Macro test strategies

## What you’ll build
A `#stringify` macro package (starter expands to a placeholder until you implement it).

## Project type
Swift Package (macro + library + CLI)

## Steps overview
1. Study macro target layout
2. Implement StringifyMacro.expansion
3. Run CLI + tests

## Stretch goals
- Add an `@attached(member)` macro that synthesizes an `init`

## Required tooling
Xcode 16+ / Swift 6; Linux may build if swift-syntax resolves (network).

## Docs (verify APIs here)
- [Macros (TSL)](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/macros/)
- [Swift Macros](https://developer.apple.com/documentation/swift/macros)

## Untested / Apple-only notes
- First `swift build` downloads swift-syntax — needs network.
- Macro expansion tests using SwiftSyntaxMacrosGenericTestSupport may need adjustment per swift-syntax version.
- Starter macro intentionally returns a placeholder tuple so scaffolding compiles before the TODO is done.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
