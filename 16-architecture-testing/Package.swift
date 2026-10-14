// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "ArchitectureTesting",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "ArchitectureTesting", targets: ["ArchitectureTesting"]),
        .executable(name: "ArchitectureTestingCLI", targets: ["ArchitectureTestingCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "ArchitectureTesting"),
        .executableTarget(name: "ArchitectureTestingCLI", dependencies: ["ArchitectureTesting"]),
        .testTarget(name: "ArchitectureTestingTests", dependencies: ["ArchitectureTesting"]),
    ]
)
