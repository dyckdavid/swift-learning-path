import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("CloudKit")
                    .font(.largeTitle.bold())
                Text("Private & public databases")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("CloudKit")
        }
    }
}

#Preview {
    ContentView()
}

