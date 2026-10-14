// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "NetworkingCodable",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "NetworkingCodable", targets: ["NetworkingCodable"]),
        .executable(name: "NetworkingCodableCLI", targets: ["NetworkingCodableCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "NetworkingCodable"),
        .executableTarget(name: "NetworkingCodableCLI", dependencies: ["NetworkingCodable"]),
        .testTarget(name: "NetworkingCodableTests", dependencies: ["NetworkingCodable"]),
    ]
)
