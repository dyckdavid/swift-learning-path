import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("App Intents")
                    .font(.largeTitle.bold())
                Text("Siri & Shortcuts")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Intents")
        }
    }
}

#Preview {
    ContentView()
}

