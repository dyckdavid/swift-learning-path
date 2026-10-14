// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "TypesAndOOP",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "TypesAndOOP", targets: ["TypesAndOOP"]),
        .executable(name: "TypesAndOOPCLI", targets: ["TypesAndOOPCLI"]),
    ],
    dependencies: [

    ],
    targets: [
        .target(name: "TypesAndOOP"),
        .executableTarget(name: "TypesAndOOPCLI", dependencies: ["TypesAndOOP"]),
        .testTarget(name: "TypesAndOOPTests", dependencies: ["TypesAndOOP"]),
    ]
)
