import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("SwiftUI Basics")
                    .font(.largeTitle.bold())
                Text("Layout, views, modifiers")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Basics")
        }
    }
}

#Preview {
    ContentView()
}

