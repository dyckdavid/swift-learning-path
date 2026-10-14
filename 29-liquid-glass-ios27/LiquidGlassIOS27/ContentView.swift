import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Liquid Glass & iOS 27")
                    .font(.largeTitle.bold())
                Text("Design + new SwiftUI APIs")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Glass")
        }
    }
}

#Preview {
    ContentView()
}

