// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "ConcurrencyLab",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "ConcurrencyLab", targets: ["ConcurrencyLab"]),
        .executable(name: "ConcurrencyLabCLI", targets: ["ConcurrencyLabCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "ConcurrencyLab"),
        .executableTarget(name: "ConcurrencyLabCLI", dependencies: ["ConcurrencyLab"]),
        .testTarget(name: "ConcurrencyLabTests", dependencies: ["ConcurrencyLab"]),
    ]
)
