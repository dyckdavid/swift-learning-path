import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("macOS App")
                    .font(.largeTitle.bold())
                Text("NavigationSplitView + Settings")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("MacNotes")
        }
    }
}

#Preview {
    ContentView()
}

