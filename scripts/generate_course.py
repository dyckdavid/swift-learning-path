#!/usr/bin/env python3
"""Generate the Swift Learning Path course scaffolding (main branch, spoiler-free)."""

from __future__ import annotations

import json
import os
import textwrap
import uuid
from pathlib import Path

ROOT = Path("/workspace")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.lstrip("\n") if content.startswith("\n") else content, encoding="utf-8")
    if not content.endswith("\n"):
        path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")


def uid() -> str:
    return uuid.uuid4().hex[:24].upper()


TODO_TEMPLATE = '''\
// MARK: - TODO: {title}
/*
 Goal:
 {goal}

 Steps:
{steps}

 Hints:
{hints}

 Acceptance criteria:
{acceptance}

 Docs:
{docs}
*/
'''


def todo_block(title: str, goal: str, steps: list[str], hints: list[str], acceptance: list[str], docs: list[str]) -> str:
    return TODO_TEMPLATE.format(
        title=title,
        goal=goal,
        steps="\n".join(f" {i}. {s}" for i, s in enumerate(steps, 1)),
        hints="\n".join(f" - {h}" for h in hints),
        acceptance="\n".join(f" - {a}" for a in acceptance),
        docs="\n".join(f" - {d}" for d in docs),
    )


def package_swift(name: str, platforms: str = '.macOS(.v14), .iOS(.v17)', extra_deps: str = "", products: str | None = None, targets: str | None = None) -> str:
    if products is None:
        products = f'''\
        .library(name: "{name}", targets: ["{name}"]),
        .executable(name: "{name}CLI", targets: ["{name}CLI"]),'''
    if targets is None:
        targets = f'''\
        .target(name: "{name}"),
        .executableTarget(name: "{name}CLI", dependencies: ["{name}"]),
        .testTarget(name: "{name}Tests", dependencies: ["{name}"]),'''
    return f'''\
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "{name}",
    platforms: [{platforms}],
    products: [
{products}
    ],
    dependencies: [
{extra_deps}
    ],
    targets: [
{targets}
    ]
)
'''


def readme_project(
    number: str,
    title: str,
    concepts: list[str],
    build: str,
    steps: list[str],
    stretch: list[str],
    xcode: str,
    untested: list[str],
    kind: str,
    docs: list[tuple[str, str]],
) -> str:
    concept_list = "\n".join(f"- {c}" for c in concepts)
    steps_list = "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    stretch_list = "\n".join(f"- {s}" for s in stretch)
    untested_list = "\n".join(f"- {u}" for u in untested) if untested else "- None flagged for this project’s Linux-verifiable pieces."
    docs_list = "\n".join(f"- [{t}]({u})" for t, u in docs)
    return f'''\
# {number}. {title}

## Concepts
{concept_list}

## What you’ll build
{build}

## Project type
{kind}

## Steps overview
{steps_list}

## Stretch goals
{stretch_list}

## Required tooling
{xcode}

## Docs (verify APIs here)
{docs_list}

## Untested / Apple-only notes
{untested_list}

## Solutions
Full implementations live on the `solutions` branch (same folder path). Keep `main` spoiler-free while you work.
'''


# Minimal Xcode project generator (iOS app)
def generate_xcode_app(
    project_dir: Path,
    name: str,
    bundle_id: str,
    sources: dict[str, str],
    deployment: str = "17.0",
    extra_frameworks: list[str] | None = None,
    entitlements: str | None = None,
    info_plist_extras: dict | None = None,
    platforms: str = "iphoneos iphonesimulator",
) -> None:
    """Create a minimal but openable .xcodeproj + sources for an iOS SwiftUI app."""
    extra_frameworks = extra_frameworks or []
    src_root = project_dir / name
    for rel, content in sources.items():
        write(src_root / rel, content)

    # Info.plist
    info = {
        "CFBundleDevelopmentRegion": "en",
        "CFBundleDisplayName": name,
        "CFBundleExecutable": "$(EXECUTABLE_NAME)",
        "CFBundleIdentifier": "$(PRODUCT_BUNDLE_IDENTIFIER)",
        "CFBundleInfoDictionaryVersion": "6.0",
        "CFBundleName": "$(PRODUCT_NAME)",
        "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": "1.0",
        "CFBundleVersion": "1",
        "LSRequiresIPhoneOS": True,
        "UIApplicationSceneManifest": {
            "UIApplicationSupportsMultipleScenes": True,
            "UISceneConfigurations": {},
        },
        "UILaunchScreen": {},
        "UISupportedInterfaceOrientations": [
            "UIInterfaceOrientationPortrait",
            "UIInterfaceOrientationLandscapeLeft",
            "UIInterfaceOrientationLandscapeRight",
        ],
    }
    if info_plist_extras:
        info.update(info_plist_extras)
    # Write as XML plist via simple JSON-like XML
    write(src_root / "Info.plist", plist_xml(info))

    if entitlements:
        write(src_root / f"{name}.entitlements", entitlements)

    # project.yml for XcodeGen (optional regeneration on Mac)
    frameworks_yaml = "\n".join(f"      - framework: {f}" for f in extra_frameworks)
    ent_yaml = f"\n    entitlements:\n      path: {name}/{name}.entitlements" if entitlements else ""
    write(project_dir / "project.yml", f'''\
name: {name}
options:
  bundleIdPrefix: com.swiftlearning
  deploymentTarget:
    iOS: "{deployment}"
settings:
  base:
    SWIFT_VERSION: "6.0"
    TARGETED_DEVICE_FAMILY: "1,2"
    GENERATE_INFOPLIST_FILE: NO
    INFOPLIST_FILE: {name}/Info.plist
    PRODUCT_BUNDLE_IDENTIFIER: {bundle_id}
targets:
  {name}:
    type: application
    platform: iOS
    sources:
      - {name}{ent_yaml}
    settings:
      base:
        PRODUCT_BUNDLE_IDENTIFIER: {bundle_id}
        INFOPLIST_FILE: {name}/Info.plist
''')

    # Hand-written pbxproj
    project_id = uid()
    target_id = uid()
    sources_phase = uid()
    frameworks_phase = uid()
    resources_phase = uid()
    project_config_list = uid()
    target_config_list = uid()
    debug_proj = uid()
    release_proj = uid()
    debug_tgt = uid()
    release_tgt = uid()
    product_ref = uid()
    main_group = uid()
    products_group = uid()
    src_group = uid()

    file_entries = []
    build_files = []
    group_children = []
    source_build = []

    for rel in sources:
        fid = uid()
        bid = uid()
        filename = Path(rel).name
        file_entries.append(f'\t\t{fid} /* {filename} */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = {filename}; sourceTree = "<group>"; }};')
        build_files.append(f'\t\t{bid} /* {filename} in Sources */ = {{isa = PBXBuildFile; fileRef = {fid} /* {filename} */; }};')
        group_children.append(f'\t\t\t\t{fid} /* {filename} */,')
        source_build.append(f'\t\t\t\t{bid} /* {filename} in Sources */,')

    info_id = uid()
    file_entries.append(f'\t\t{info_id} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};')
    group_children.append(f'\t\t\t\t{info_id} /* Info.plist */,')

    ent_id = None
    if entitlements:
        ent_id = uid()
        file_entries.append(f'\t\t{ent_id} /* {name}.entitlements */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.entitlements; path = {name}.entitlements; sourceTree = "<group>"; }};')
        group_children.append(f'\t\t\t\t{ent_id} /* {name}.entitlements */,')

    file_entries.append(f'\t\t{product_ref} /* {name}.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = {name}.app; sourceTree = BUILT_PRODUCTS_DIR; }};')

    code_sign_ent = f"\n\t\t\t\tCODE_SIGN_ENTITLEMENTS = {name}/{name}.entitlements;" if entitlements else ""

    pbx = f'''\
// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
{chr(10).join(build_files)}
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
{chr(10).join(file_entries)}
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		{frameworks_phase} /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		{main_group} = {{
			isa = PBXGroup;
			children = (
				{src_group} /* {name} */,
				{products_group} /* Products */,
			);
			sourceTree = "<group>";
		}};
		{products_group} /* Products */ = {{
			isa = PBXGroup;
			children = (
				{product_ref} /* {name}.app */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
		{src_group} /* {name} */ = {{
			isa = PBXGroup;
			children = (
{chr(10).join(group_children)}
			);
			path = {name};
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		{target_id} /* {name} */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {target_config_list} /* Build configuration list for PBXNativeTarget "{name}" */;
			buildPhases = (
				{sources_phase} /* Sources */,
				{frameworks_phase} /* Frameworks */,
				{resources_phase} /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = {name};
			productName = {name};
			productReference = {product_ref} /* {name}.app */;
			productType = "com.apple.product-type.application";
		}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		{project_id} /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1600;
				LastUpgradeCheck = 1600;
			}};
			buildConfigurationList = {project_config_list} /* Build configuration list for PBXProject "{name}" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = {main_group};
			productRefGroup = {products_group} /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				{target_id} /* {name} */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		{resources_phase} /* Resources */ = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		{sources_phase} /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
{chr(10).join(source_build)}
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		{debug_proj} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ENABLE_MODULES = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_TESTABILITY = YES;
				GCC_DYNAMIC_NO_PIC = NO;
				IPHONEOS_DEPLOYMENT_TARGET = {deployment};
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				SWIFT_VERSION = 6.0;
			}};
			name = Debug;
		}};
		{release_proj} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ENABLE_MODULES = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				IPHONEOS_DEPLOYMENT_TARGET = {deployment};
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_VERSION = 6.0;
				VALIDATE_PRODUCT = YES;
			}};
			name = Release;
		}};
		{debug_tgt} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;{code_sign_ent}
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = {name}/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {bundle_id};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SUPPORTED_PLATFORMS = "{platforms}";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Debug;
		}};
		{release_tgt} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				CODE_SIGN_STYLE = Automatic;{code_sign_ent}
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = {name}/Info.plist;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = {bundle_id};
				PRODUCT_NAME = "$(TARGET_NAME)";
				SUPPORTED_PLATFORMS = "{platforms}";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 6.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		{project_config_list} /* Build configuration list for PBXProject "{name}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{debug_proj} /* Debug */,
				{release_proj} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{target_config_list} /* Build configuration list for PBXNativeTarget "{name}" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{debug_tgt} /* Debug */,
				{release_tgt} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */
	}};
	rootObject = {project_id} /* Project object */;
}}
'''
    write(project_dir / f"{name}.xcodeproj" / "project.pbxproj", pbx)

    # Flatten sources into single folder for pbx path simplicity
    # Move nested files: our pbx assumes flat filenames in {name}/
    # If sources had nested paths, rewrite to flat
    for rel in list(sources.keys()):
        if "/" in rel:
            nested = src_root / rel
            flat = src_root / Path(rel).name
            if nested.exists() and nested != flat:
                flat.write_text(nested.read_text(encoding="utf-8"), encoding="utf-8")
                nested.unlink()
                # clean empty dirs
                try:
                    nested.parent.rmdir()
                except OSError:
                    pass


def plist_xml(data: dict) -> str:
    def render(value, indent=0) -> str:
        sp = "\t" * indent
        if isinstance(value, dict):
            lines = [f"{sp}<dict>"]
            for k, v in value.items():
                lines.append(f"{sp}\t<key>{k}</key>")
                lines.append(render(v, indent + 1))
            lines.append(f"{sp}</dict>")
            return "\n".join(lines)
        if isinstance(value, list):
            lines = [f"{sp}<array>"]
            for item in value:
                lines.append(render(item, indent + 1))
            lines.append(f"{sp}</array>")
            return "\n".join(lines)
        if isinstance(value, bool):
            return f"{sp}<{'true' if value else 'false'}/>"
        if isinstance(value, int):
            return f"{sp}<integer>{value}</integer>"
        return f"{sp}<string>{value}</string>"

    return f'''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
{render(data)}
</plist>
'''


APP_STUB = '''\
import SwiftUI

@main
struct __NAME__App: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
'''

CONTENT_STUB_HEADER = '''\
import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("__TITLE__")
                    .font(.largeTitle.bold())
                Text("__SUBTITLE__")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("__NAV__")
        }
    }
}

#Preview {
    ContentView()
}

'''


def app_sources(name: str, title: str, subtitle: str, nav: str, extra_swift: str = "") -> dict[str, str]:
    sources = {
        f"{name}App.swift": APP_STUB.replace("__NAME__", name),
        "ContentView.swift": (
            CONTENT_STUB_HEADER
            .replace("__TITLE__", title)
            .replace("__SUBTITLE__", subtitle)
            .replace("__NAV__", nav)
        ),
    }
    if extra_swift.strip():
        # Keep imports valid: assignment/starter helpers live in a sibling file.
        sources["Assignment.swift"] = extra_swift.lstrip("\n")
    return sources


# ---------------------------------------------------------------------------
# Projects
# ---------------------------------------------------------------------------

def project_01():
    d = ROOT / "01-swift-basics"
    name = "SwiftBasics"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "SwiftBasics.swift", f'''\
/// Project 01 — Swift basics: types, optionals, collections.
/// Open this folder in Xcode (File → Open → Package.swift) or use `swift build` / `swift test`.

public enum TemperatureUnit: String, Sendable {{
    case celsius
    case fahrenheit
}}

public struct MeasurementSample: Equatable, Sendable {{
    public var value: Double
    public var unit: TemperatureUnit

    public init(value: Double, unit: TemperatureUnit) {{
        self.value = value
        self.unit = unit
    }}
}}

public enum BasicsExercises {{
    /// Starter helper used by tests — keep compiling while you fill in TODOs.
    public static func greet(name: String) -> String {{
        "Hello, \\(name)!"
    }}

{todo_block(
    "Optionals and nil-coalescing",
    "Parse an optional Int from a String and provide a default.",
    [
        "Implement `parseScore(_:default:)` below (uncomment and fill in).",
        "Return the Int value when parsing succeeds; otherwise return `defaultValue`.",
        "Call your function from the CLI target for a quick smoke check.",
    ],
    [
        "Use `Int(_:)` which returns `Int?`.",
        "Prefer `??` or `guard let` — both are fine.",
    ],
    [
        "`parseScore(\"42\", default: 0) == 42`",
        "`parseScore(\"abc\", default: 0) == 0`",
    ],
    [
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/",
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/optionals/",
    ],
)}
    // public static func parseScore(_ text: String, default defaultValue: Int) -> Int {{
    //     fatalError("TODO")
    // }}

{todo_block(
    "Collections",
    "Build a frequency dictionary from an array of words (case-insensitive).",
    [
        "Implement `wordFrequencies(in:)` returning `[String: Int]`.",
        "Normalize keys with `lowercased()`.",
        "Ignore empty strings after trimming whitespace.",
    ],
    [
        "Start with `[:]` and mutate counts, or use `reduce(into:)`.",
        "`trimmingCharacters(in: .whitespacesAndNewlines)` is useful.",
    ],
    [
        "`wordFrequencies(in: [\"Hi\", \"hi\", \" \", \"Yo\"]) == [\"hi\": 2, \"yo\": 1]`",
    ],
    [
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collectiontypes/",
    ],
)}
    // public static func wordFrequencies(in words: [String]) -> [String: Int] {{
    //     fatalError("TODO")
    // }}

{todo_block(
    "Convert temperatures",
    "Convert a MeasurementSample between Celsius and Fahrenheit.",
    [
        "Implement `converted(_:to:)`.",
        "If units already match, return the input unchanged.",
        "C→F: `c * 9/5 + 32`. F→C: `(f - 32) * 5/9`.",
    ],
    [
        "Keep the result in a new `MeasurementSample`.",
    ],
    [
        "Converting 0°C to Fahrenheit yields 32.",
        "Converting 32°F to Celsius yields 0.",
    ],
    [
        "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/functions/",
    ],
)}
    // public static func converted(_ sample: MeasurementSample, to unit: TemperatureUnit) -> MeasurementSample {{
    //     fatalError("TODO")
    // }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", f'''\
import {name}

print(BasicsExercises.greet(name: "David"))
print("Project 01 starter is running. Uncomment TODOs in Sources/{name}/SwiftBasics.swift")
''')
    write(d / "Tests" / f"{name}Tests" / "SwiftBasicsTests.swift", f'''\
import Testing
@testable import {name}

@Test func greetWorks() {{
    #expect(BasicsExercises.greet(name: "David") == "Hello, David!")
}}

// Uncomment as you implement TODOs:
// @Test func parseScore() {{
//     #expect(BasicsExercises.parseScore("42", default: 0) == 42)
//     #expect(BasicsExercises.parseScore("nope", default: 7) == 7)
// }}
''')
    write(d / "README.md", readme_project(
        "01", "Swift Basics — Types, Optionals, Collections",
        ["Value types & type inference", "Optionals / if-let / guard / ??", "Array, Set, Dictionary", "String basics"],
        "Small library helpers (greeting, score parsing, word frequencies, temperature conversion) with tests.",
        ["Open Package.swift in Xcode or `cd 01-swift-basics && swift test`", "Read starter types", "Implement each TODO block", "Uncomment matching tests"],
        ["Add a `Set`-based unique-word counter", "Support Kelvin in temperature conversion"],
        "**Xcode 16+** (Swift 6) recommended; **Xcode 27** preferred for the rest of the course. Linux: `swift build` / `swift test` verified when possible.",
        ["Apple-only UI not used here."],
        "Swift Package (library + executable + tests)",
        [
            ("The Swift Programming Language — The Basics", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/"),
            ("Optionals", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/optionals/"),
            ("Collection Types", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/collectiontypes/"),
        ],
    ))


def project_02():
    d = ROOT / "02-functions-closures"
    name = "FunctionsClosures"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "FunctionsClosures.swift", f'''\
public enum MathOps {{
    public static func identity(_ value: Int) -> Int {{ value }}

{todo_block(
    "Higher-order functions",
    "Implement map/filter/reduce-style helpers without calling the stdlib versions for practice (or call them — your choice; document which).",
    [
        "Implement `squaredEvens(in:)` → squares of even numbers, preserving order.",
        "Implement `sum(of:using:)` that reduces `[Int]` with a closure `(Int, Int) -> Int`.",
    ],
    [
        "`filter` then `map` is fine.",
        "Default the sum operator to `+` via a default parameter if you like.",
    ],
    [
        "`squaredEvens(in: [1,2,3,4]) == [4, 16]`",
        "`sum(of: [1,2,3], using: +) == 6`",
    ],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/"],
)}
    // public static func squaredEvens(in values: [Int]) -> [Int] {{ fatalError("TODO") }}
    // public static func sum(of values: [Int], using combine: (Int, Int) -> Int) -> Int {{ fatalError("TODO") }}

{todo_block(
    "Escaping closures & trailing syntax",
    "Run an async-looking completion on a success path (still synchronous for this exercise).",
    [
        "Implement `perform(success:failure:)` that calls `success(\"ok\")` when `shouldSucceed` is true, else `failure`.",
        "Mark closures `@escaping` if stored; here they are called immediately so escaping is optional — use it if you store them.",
    ],
    ["Practice trailing-closure call sites in the CLI."],
    ["Success path returns the string from the success closure to the caller."],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/"],
)}
    // Toggle in CLI/tests when implementing the TODO below.
    nonisolated(unsafe) public static var shouldSucceed: Bool = true
    // public static func perform(success: (String) -> String, failure: () -> String) -> String {{ fatalError("TODO") }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", f'''\
import {name}
print("2² identity check:", MathOps.identity(4))
''')
    write(d / "Tests" / f"{name}Tests" / "FunctionsClosuresTests.swift", f'''\
import Testing
@testable import {name}

@Test func identity() {{
    #expect(MathOps.identity(9) == 9)
}}
''')
    write(d / "README.md", readme_project(
        "02", "Functions, Control Flow & Closures",
        ["Functions & parameters", "Closures / trailing closures", "map/filter/reduce mindset", "Escaping vs non-escaping"],
        "Reusable math helpers driven by closures, plus a tiny success/failure callback exercise.",
        ["Implement `squaredEvens` and `sum`", "Wire CLI demos", "Add tests"],
        ["Rewrite with `compactMap`", "Add a generic `map` helper"],
        "Xcode 16+ / Swift 6; Linux `swift test` OK.",
        [],
        "Swift Package",
        [("Closures", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/"),
         ("Control Flow", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/controlflow/")],
    ))


def project_03():
    d = ROOT / "03-types-and-oop"
    name = "TypesAndOOP"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "TypesAndOOP.swift", f'''\
public struct Point: Equatable, Sendable {{
    public var x: Double
    public var y: Double
    public init(x: Double, y: Double) {{ self.x = x; self.y = y }}
}}

public enum Shape: Equatable, Sendable {{
    case circle(radius: Double)
    case rectangle(width: Double, height: Double)
}}

public final class Counter: @unchecked Sendable {{
    public private(set) var value: Int
    public init(value: Int = 0) {{ self.value = value }}
    public func increment() {{ value += 1 }}
}}

public enum TypeExercises {{
{todo_block(
    "Enum methods & computed properties",
    "Add area computation for Shape.",
    ["Implement `area(of:)` for circle (πr²) and rectangle (w×h).", "Use `Double.pi`."],
    ["Switch must be exhaustive."],
    ["Circle r=1 → π", "Rectangle 3×4 → 12"],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/enumerations/"],
)}
    // public static func area(of shape: Shape) -> Double {{ fatalError("TODO") }}

{todo_block(
    "Value vs reference semantics",
    "Demonstrate copying a Point vs sharing a Counter.",
    ["Implement `moved(_ :by:)` returning a new Point offset by dx/dy without mutating the input.",
     "Implement `bumpTwice(_:)` that increments the same Counter instance twice and returns its value."],
    ["Structs copy; classes share identity."],
    ["Point(0,0) moved by (1,2) → (1,2) and original stays (0,0)."],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/"],
)}
    // public static func moved(_ point: Point, by delta: Point) -> Point {{ fatalError("TODO") }}
    // public static func bumpTwice(_ counter: Counter) -> Int {{ fatalError("TODO") }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", "import TypesAndOOP\nprint(Point(x: 1, y: 2))\n")
    write(d / "Tests" / f"{name}Tests" / "TypesAndOOPTests.swift", '''\
import Testing
@testable import TypesAndOOP

@Test func counterIncrements() {
    let c = Counter()
    c.increment()
    #expect(c.value == 1)
}
''')
    write(d / "README.md", readme_project(
        "03", "Structs, Classes & Enums",
        ["Structs vs classes", "Enums with associated values", "Mutability & identity", "Equatable / Sendable basics"],
        "Geometry shapes + a reference-type Counter to feel value vs reference semantics.",
        ["Implement area", "Implement move/bump helpers", "Write tests proving copy vs share"],
        ["Add `triangle` case", "Make Counter an actor preview for project 05"],
        "Xcode 16+ / Swift 6; Linux OK.",
        [],
        "Swift Package",
        [("Structures and Classes", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/classesandstructures/"),
         ("Enumerations", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/enumerations/")],
    ))


def project_04():
    d = ROOT / "04-protocols-generics-errors"
    name = "ProtocolsGenerics"
    write(d / "Package.swift", package_swift(name))
    write(d / "Sources" / name / "ProtocolsGenerics.swift", f'''\
public protocol IdentifiableItem: Sendable {{
    var id: String {{ get }}
}}

public struct User: IdentifiableItem, Equatable, Sendable {{
    public let id: String
    public var name: String
    public init(id: String, name: String) {{ self.id = id; self.name = name }}
}}

public enum StoreError: Error, Equatable, Sendable {{
    case notFound(id: String)
    case emptyName
}}

public struct MemoryStore<Item: IdentifiableItem>: Sendable {{
    private var items: [String: Item]
    public init(items: [Item] = []) {{
        self.items = Dictionary(uniqueKeysWithValues: items.map {{ ($0.id, $0) }})
    }}

    public func all() -> [Item] {{ Array(items.values) }}

{todo_block(
    "Generics + throwing APIs",
    "Complete store operations with typed errors.",
    ["Implement `item(id:)` throwing `StoreError.notFound`.",
     "Implement `upsert` mutating method.",
     "Implement free function `validatedName(_:)` that throws `emptyName` for blank strings."],
    ["Use `guard let` + `throw`.", "Trim whitespace before validating names."],
    ["Missing id throws `.notFound`", "\"   \" throws `.emptyName`"],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/",
     "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/",
     "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/"],
)}
    // public func item(id: String) throws -> Item {{ fatalError("TODO") }}
    // public mutating func upsert(_ item: Item) {{ fatalError("TODO") }}
}}

// public func validatedName(_ raw: String) throws -> String {{ fatalError("TODO") }}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", "import ProtocolsGenerics\nprint(User(id: \"1\", name: \"David\"))\n")
    write(d / "Tests" / f"{name}Tests" / "ProtocolsGenericsTests.swift", '''\
import Testing
@testable import ProtocolsGenerics

@Test func storeStartsEmpty() {
    let store = MemoryStore<User>()
    #expect(store.all().isEmpty)
}
''')
    write(d / "README.md", readme_project(
        "04", "Protocols, Generics & Errors",
        ["Protocol-oriented design", "Generics & constraints", "throws / Result mindset", "Equatable errors"],
        "A tiny in-memory generic store with validation errors.",
        ["Implement fetch/upsert/validate", "Cover error paths in tests"],
        ["Add `remove(id:)`", "Express failures with `Result` as an alternate API"],
        "Xcode 16+ / Swift 6; Linux OK.",
        [],
        "Swift Package",
        [("Protocols", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/"),
         ("Generics", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/generics/"),
         ("Error Handling", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/")],
    ))


def project_05():
    d = ROOT / "05-concurrency"
    name = "ConcurrencyLab"
    write(d / "Package.swift", package_swift(name, platforms=".macOS(.v14), .iOS(.v17)"))
    write(d / "Sources" / name / "ConcurrencyLab.swift", f'''\
public actor ScoreBoard: Sendable {{
    private var scores: [String: Int] = [:]

    public init() {{}}

    public func setScore(_ score: Int, for player: String) {{
        scores[player] = score
    }}

    public func score(for player: String) -> Int? {{
        scores[player]
    }}

{todo_block(
    "Actor isolation",
    "Add a method that increments a player's score safely inside the actor.",
    ["Implement `addPoints(_:to:)` on ScoreBoard.", "If player missing, start from 0."],
    ["All mutable state stays inside the actor."],
    ["Concurrent increments do not data-race (Swift 6 default isolation)."],
    ["https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/",
     "https://developer.apple.com/documentation/swift/actor"],
)}
    // public func addPoints(_ points: Int, to player: String) {{ fatalError("TODO") }}
}}

public enum AsyncExercises {{
{todo_block(
    "async/await + TaskGroup",
    "Fetch multiple fake resources concurrently and collect results.",
    ["Implement `loadAll(ids:)` using `withTaskGroup`.",
     "Each child calls `fakeFetch(id:)` below.",
     "Return results sorted by id."],
    ["`fakeFetch` already exists — reuse it.", "Prefer structured concurrency over detached tasks."],
    ["Order of returned array is sorted by id regardless of completion order."],
    ["https://developer.apple.com/documentation/swift/taskgroup",
     "https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/"],
)}
    public static func fakeFetch(id: String) async -> (id: String, value: Int) {{
        try? await Task.sleep(for: .milliseconds(10))
        return (id, id.count)
    }}

    // public static func loadAll(ids: [String]) async -> [(id: String, value: Int)] {{ fatalError("TODO") }}
}}
''')
    write(d / "Sources" / f"{name}CLI" / "main.swift", '''\
import ConcurrencyLab

let board = ScoreBoard()
await board.setScore(10, for: "David")
print(await board.score(for: "David") ?? -1)
''')
    write(d / "Tests" / f"{name}Tests" / "ConcurrencyLabTests.swift", '''\
import Testing
@testable import ConcurrencyLab

@Test func fakeFetchReturnsLength() async {
    let result = await AsyncExercises.fakeFetch(id: "abcd")
    #expect(result.value == 4)
}
''')
    write(d / "README.md", readme_project(
        "05", "Concurrency — async/await, Actors, Swift 6",
        ["async/await", "actors & isolation", "Task / TaskGroup", "Swift 6 strict concurrency / Sendable"],
        "An actor-backed scoreboard and a concurrent fan-out loader.",
        ["Implement actor increment", "Implement TaskGroup loader", "Enable complete concurrency checking in Xcode if needed"],
        ["Add `AsyncSequence` ticker", "Experiment with `@MainActor` UI boundary types (preview for SwiftUI projects)"],
        "Xcode 16+ with Swift 6 language mode; Linux `swift test` OK for this package.",
        ["UIKit/SwiftUI main-actor UI not covered here."],
        "Swift Package (Swift 6)",
        [("Concurrency", "https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/"),
         ("Swift 6 concurrency migration guide", "https://www.swift.org/migration/documentation/swift-6-concurrency-migration-guide/"),
         ("actor", "https://developer.apple.com/documentation/swift/actor")],
    ))


def main() -> None:
    print("Generating projects 01-05...")
    project_01()
    project_02()
    project_03()
    project_04()
    project_05()
    print("01-05 done")


if __name__ == "__main__":
    main()
