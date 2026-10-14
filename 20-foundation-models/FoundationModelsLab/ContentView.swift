import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Foundation Models")
                    .font(.largeTitle.bold())
                Text("Apple Intelligence on-device")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Summarize")
        }
    }
}

#Preview {
    ContentView()
}

