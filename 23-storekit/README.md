# 23. StoreKit 2 In-App Purchases

## Concepts
- Product.products
- purchase()
- Transaction.finish
- currentEntitlements
- StoreKit Configuration testing

## What you’ll build
A tiny shop that unlocks “Pro Themes”.

## Project type
Xcode iOS app

## Steps overview
1. Attach Products.storekit to the scheme
2. Implement purchase + entitlements UI
3. Test cancel/pending paths

## Stretch goals
- Subscriptions with SubscriptionStoreView
- Offer codes (advanced)

## Required tooling
Xcode 27 + StoreKit Testing.

## Docs (verify APIs here)
- [StoreKit](https://developer.apple.com/documentation/storekit)
- [Product.purchase](https://developer.apple.com/documentation/storekit/product/purchase(options:))
- [Transaction](https://developer.apple.com/documentation/storekit/transaction)

## Untested / Apple-only notes
- Cannot purchase-test on Linux.
- StoreKit Configuration JSON may need slight tweaks if Xcode migrates the format — let Xcode re-save if it prompts.

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
