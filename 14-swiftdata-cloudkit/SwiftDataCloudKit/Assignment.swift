import Foundation
import SwiftData

@Model
final class SyncedTask {
    var title: String
    var isDone: Bool
    init(title: String, isDone: Bool = false) {
        self.title = title
        self.isDone = isDone
    }
}
