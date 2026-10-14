import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            ProfileForm()
                .navigationTitle("Profile")
        }
    }
}

#Preview { ContentView() }
