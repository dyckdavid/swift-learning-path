import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("watchOS Companion Host")
                    .font(.largeTitle.bold())
                Text("Add Watch target in Xcode")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Host")
        }
    }
}

#Preview {
    ContentView()
}

