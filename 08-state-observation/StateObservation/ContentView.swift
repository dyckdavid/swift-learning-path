import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("State & Observation")
                    .font(.largeTitle.bold())
                Text("@Observable, @State, bindings")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Counter")
        }
    }
}

#Preview {
    ContentView()
}

