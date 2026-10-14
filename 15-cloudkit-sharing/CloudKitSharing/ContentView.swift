import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("CloudKit Sharing")
                    .font(.largeTitle.bold())
                Text("CKShare & shared DB")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Sharing")
        }
    }
}

#Preview {
    ContentView()
}

