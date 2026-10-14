import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Push Notifications")
                    .font(.largeTitle.bold())
                Text("UserNotifications + APNs")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Push")
        }
    }
}

#Preview {
    ContentView()
}

