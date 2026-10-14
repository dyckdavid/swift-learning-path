import UserNotifications
// MARK: - TODO: Local + remote notification plumbing
/*
 Goal:
 Request authorization, register for remote notifications, handle foreground presentation.

 Steps:
 1. Ask for notification permission with `UNUserNotificationCenter`.
 2. Schedule a **local** notification as a first milestone.
 3. Call `UIApplication.shared.registerForRemoteNotifications()` and implement delegate to receive device token.
 4. Document how you’d send a test push via CloudKit / APNs provider / Push Notification Console.
 5. Implement `UNUserNotificationCenterDelegate` for foreground display.

 Hints:
 - Remote pushes need Apple Developer push capability + a server or Push Console.
 - Start with local notifications so you learn the UX without a server.

 Acceptance criteria:
 - Local notification appears; app logs device token when registered.

 Docs:
 - https://developer.apple.com/documentation/usernotifications
 - https://developer.apple.com/documentation/usernotifications/unusernotificationcenter
 - https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns
 - https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications
*/
