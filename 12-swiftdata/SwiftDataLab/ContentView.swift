import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("SwiftData")
                    .font(.largeTitle.bold())
                Text("Local persistence")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Notes")
        }
    }
}

#Preview {
    ContentView()
}

