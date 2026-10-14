import SwiftUI

struct ProfileForm: View {
    @State private var name = ""
    @State private var difficulty = 1
    @State private var notifications = true
    @State private var showAlert = false

    private var canSave: Bool {
        !name.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty
    }

    var body: some View {
        Form {
            Section("Profile") {
                TextField("Display name", text: $name)
                Picker("Difficulty", selection: $difficulty) {
                    Text("Easy").tag(0)
                    Text("Normal").tag(1)
                    Text("Hard").tag(2)
                }
                Toggle("Notifications", isOn: $notifications)
            }
            Button("Save") { showAlert = true }
                .disabled(!canSave)
        }
        .alert("Saved", isPresented: $showAlert) {
            Button("OK", role: .cancel) {}
        } message: {
            Text("\(name) · difficulty \(difficulty) · notifications \(notifications)")
        }
    }
}
