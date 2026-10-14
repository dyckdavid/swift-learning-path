import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Accessibility")
                    .font(.largeTitle.bold())
                Text("VoiceOver & Dynamic Type")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("A11y")
        }
    }
}

#Preview {
    ContentView()
}

