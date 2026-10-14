// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "FunctionsClosures",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "FunctionsClosures", targets: ["FunctionsClosures"]),
        .executable(name: "FunctionsClosuresCLI", targets: ["FunctionsClosuresCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "FunctionsClosures"),
        .executableTarget(name: "FunctionsClosuresCLI", dependencies: ["FunctionsClosures"]),
        .testTarget(name: "FunctionsClosuresTests", dependencies: ["FunctionsClosures"]),
    ]
)
