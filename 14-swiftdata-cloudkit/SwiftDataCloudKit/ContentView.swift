import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("SwiftData + CloudKit")
                    .font(.largeTitle.bold())
                Text("Private DB sync")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Tasks")
        }
    }
}

#Preview {
    ContentView()
}

