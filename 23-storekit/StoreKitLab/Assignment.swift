import StoreKit
// MARK: - TODO: StoreKit 2 purchase + entitlements
/*
 Goal:
 Load products, purchase, and unlock content via Transaction APIs.

 Steps:
 1. Create an StoreKit Configuration file in Xcode (`.storekit`) with a non-consumable product id.
 2. `let products = try await Product.products(for: ids)`
 3. Call `try await product.purchase()` and handle `Product.PurchaseResult`.
 4. On verified success, unlock content and `await transaction.finish()`.
 5. Listen to `Transaction.updates` / use `Transaction.currentEntitlements` to restore state.
 6. Optional SwiftUI: `ProductView` / `StoreView` + `onInAppPurchaseCompletion`.

 Hints:
 - Use StoreKit Testing in Xcode — no App Store Connect product required for local testing.
 - Never invent receipt-parsing APIs from StoreKit 1.

 Acceptance criteria:
 - Purchasing in the local StoreKit config unlocks a feature flag in the UI.

 Docs:
 - https://developer.apple.com/documentation/storekit
 - https://developer.apple.com/documentation/storekit/product
 - https://developer.apple.com/documentation/storekit/product/purchase(options:)
 - https://developer.apple.com/documentation/storekit/transaction
 - https://developer.apple.com/storekit/
*/
