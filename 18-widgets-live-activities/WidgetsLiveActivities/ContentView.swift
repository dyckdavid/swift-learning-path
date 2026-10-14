import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Text("Widgets & Live Activities")
                    .font(.largeTitle.bold())
                Text("WidgetKit + ActivityKit")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                // Starter UI compiles. Implement TODOs below.
                Spacer()
            }
            .padding()
            .navigationTitle("Focus")
        }
    }
}

#Preview {
    ContentView()
}

