# 11. Networking + Codable

## Concepts
- URLSession async APIs
- Codable / JSONDecoder
- Protocol-based test doubles
- HTTP status handling

## What you’ll build
A PostClient against JSONPlaceholder (or fixtures).

## Project type
Swift Package

## Steps overview
1. Implement fetchPosts
2. Test with FixtureSession
3. Optional: run CLI live fetch

## Stretch goals
- Add createPost with POST + encode
- Map errors to a domain enum

## Required tooling
Xcode 16+ / Swift 6; **Linux `swift test` OK** for fixtures.

## Docs (verify APIs here)
- [URLSession](https://developer.apple.com/documentation/foundation/urlsession)
- [Codable](https://developer.apple.com/documentation/foundation/codable)

## Untested / Apple-only notes
- Live network calls depend on jsonplaceholder.typicode.com availability.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
