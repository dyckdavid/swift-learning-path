import Foundation
import Testing
@testable import NetworkingCodable

@Test func fixtureRoundTrip() throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let posts = try JSONDecoder().decode([RemotePost].self, from: json)
    #expect(posts.first?.id == 1)
}

@Test func fetchPostsUsesFixture() async throws {
    let json = Data(#"[{"id":1,"title":"t","body":"b"}]"#.utf8)
    let client = PostClient(session: FixtureSession(data: json))
    let posts = try await client.fetchPosts()
    #expect(posts.count == 1)
}
