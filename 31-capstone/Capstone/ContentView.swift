import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Capstone — StudyPilot")
                    .font(.largeTitle.bold())
                Text("Combine the course into one app")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("StudyPilot")
        }
    }
}

#Preview {
    ContentView()
}

