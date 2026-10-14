// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "ProtocolsGenerics",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "ProtocolsGenerics", targets: ["ProtocolsGenerics"]),
        .executable(name: "ProtocolsGenericsCLI", targets: ["ProtocolsGenericsCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "ProtocolsGenerics"),
        .executableTarget(name: "ProtocolsGenericsCLI", dependencies: ["ProtocolsGenerics"]),
        .testTarget(name: "ProtocolsGenericsTests", dependencies: ["ProtocolsGenerics"]),
    ]
)
