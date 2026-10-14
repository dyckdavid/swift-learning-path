import SwiftUI
import Observation

@Observable
final class CounterModel {
    var count: Int = 0
    var isHighlighted: Bool = false
    func increment(by amount: Int = 1) { count += amount }
    func reset() { count = 0 }
}

struct ContentView: View {
    @State private var model = CounterModel()

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                Text("\(model.count)")
                    .font(.largeTitle.bold())
                    .foregroundStyle(model.isHighlighted ? .orange : .primary)
                HStack {
                    Button("−") { model.increment(by: -1) }
                    Button("+") { model.increment() }
                    Button("Reset") { model.reset() }
                }
                .buttonStyle(.borderedProminent)
                Toggle("Highlight", isOn: Bindable(model).isHighlighted)
            }
            .padding()
            .navigationTitle("Counter")
        }
    }
}

#Preview { ContentView() }
