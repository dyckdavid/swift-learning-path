import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Navigation & Lists")
                    .font(.largeTitle.bold())
                Text("Stack navigation + List")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Library")
        }
    }
}

#Preview {
    ContentView()
}

