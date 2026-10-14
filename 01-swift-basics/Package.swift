// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SwiftBasics",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "SwiftBasics", targets: ["SwiftBasics"]),
        .executable(name: "SwiftBasicsCLI", targets: ["SwiftBasicsCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "SwiftBasics"),
        .executableTarget(name: "SwiftBasicsCLI", dependencies: ["SwiftBasics"]),
        .testTarget(name: "SwiftBasicsTests", dependencies: ["SwiftBasics"]),
    ]
)
