// swift-tools-version: 6.0
import PackageDescription

// Root umbrella package so `swift build` works from 17-modularization/
let package = Package(
    name: "ModularWorkspace",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "Core", targets: ["Core"]),
        .library(name: "FeatureTodos", targets: ["FeatureTodos"]),
        .executable(name: "AppShell", targets: ["AppShell"]),
    ],
    targets: [
        .target(name: "Core"),
        .target(name: "FeatureTodos", dependencies: ["Core"]),
        .executableTarget(name: "AppShell", dependencies: ["FeatureTodos", "Core"]),
        .testTarget(name: "CoreTests", dependencies: ["Core"]),
    ]
)
