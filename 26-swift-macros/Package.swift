// swift-tools-version: 6.0
import PackageDescription
import CompilerPluginSupport

let package = Package(
    name: "SwiftMacrosLab",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "SwiftMacrosLab", targets: ["SwiftMacrosLab"]),
        .executable(name: "SwiftMacrosLabCLI", targets: ["SwiftMacrosLabCLI"]),
    ],
    dependencies: [
        .package(url: "https://github.com/swiftlang/swift-syntax.git", from: "600.0.0"),
    ],
    targets: [
        .macro(
            name: "SwiftMacrosLabMacros",
            dependencies: [
                .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
                .product(name: "SwiftCompilerPlugin", package: "swift-syntax"),
            ]
        ),
        .target(name: "SwiftMacrosLab", dependencies: ["SwiftMacrosLabMacros"]),
        .executableTarget(name: "SwiftMacrosLabCLI", dependencies: ["SwiftMacrosLab"]),
        .testTarget(name: "SwiftMacrosLabTests", dependencies: [
            "SwiftMacrosLab",
            "SwiftMacrosLabMacros",
            .product(name: "SwiftSyntaxMacrosGenericTestSupport", package: "swift-syntax"),
        ]),
    ]
)
