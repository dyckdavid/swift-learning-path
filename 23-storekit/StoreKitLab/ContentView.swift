import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("StoreKit 2")
                    .font(.largeTitle.bold())
                Text("In-app purchases")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Shop")
        }
    }
}

#Preview {
    ContentView()
}

