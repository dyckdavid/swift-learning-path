# 24. Push Notifications

## Concepts
- UNUserNotificationCenter
- Authorization
- Device tokens
- APNs
- Foreground delegation

## What you’ll build
Permission flow + local notification + remote registration hooks.

## Project type
Xcode iOS app

## Steps overview
1. Implement auth + local schedule
2. Enable Push capability with your team
3. Capture device token

## Stretch goals
- Notification Service Extension for rich media
- ActivityKit push for Live Activities

## Required tooling
Xcode 27 + Developer account for remote push.

## Docs (verify APIs here)
- [User Notifications](https://developer.apple.com/documentation/usernotifications)
- [Sending to APNs](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns)

## Untested / Apple-only notes
- Remote delivery not verifiable here.
- Entitlements use development aps-environment.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
