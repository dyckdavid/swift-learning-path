import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            VStack(spacing: 16) {
                Image(systemName: "person.circle.fill")
                    .font(.system(size: 72))
                    .foregroundStyle(.tint)
                Text("David")
                    .font(.title.bold())
                Text("Learning Swift from fundamentals to pro-level apps.")
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                Spacer()
            }
            .padding()
            .navigationTitle("Basics")
        }
    }
}

#Preview { ContentView() }
