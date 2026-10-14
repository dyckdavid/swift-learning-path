import Foundation
import Testing
@testable import NetworkingCodable

@Test func fixtureRoundTrip() throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let posts = try JSONDecoder().decode([RemotePost].self, from: json)
    #expect(posts.first?.id == 1)
}
