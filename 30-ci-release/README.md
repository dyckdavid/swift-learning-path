# 30. CI, TestFlight & App Store Release

## Concepts
- Xcode Cloud workflows
- fastlane alternative
- TestFlight
- App Store Connect metadata
- Export compliance / privacy

## What you’ll build
A release playbook + sample config stubs you will customize for one of your earlier apps.

## Project type
Documentation + CI templates (no runnable iOS build here)

## Steps overview
1. Pick one app project (e.g. 12 or 31) as the release candidate
2. Fill `RELEASE_CHECKLIST.md`
3. Either configure Xcode Cloud (`ci_scripts` / workflow in App Store Connect) **or** adapt the sample Fastfile
4. Create a TestFlight internal build
5. Draft App Store listing fields (no need to submit publicly)

## Stretch goals
- Automated UI tests in CI
- Marketing screenshots via Xcode

## Required tooling
Xcode 27 + Apple Developer Program membership.

## Docs (verify APIs here)
- [Xcode Cloud](https://developer.apple.com/xcode-cloud/)
- [TestFlight](https://developer.apple.com/testflight/)
- [Distributing your app for beta testing and releases](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases)
- [fastlane docs](https://docs.fastlane.tools/)

## Untested / Apple-only notes
- No real App Store Connect push from this environment.
- Xcode Cloud requires linking the GitHub repo in Apple Developer portals.
- fastlane needs Ruby gems + credentials — treat sample as a template.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
