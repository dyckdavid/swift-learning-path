import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking
#endif

public struct RemotePost: Codable, Equatable, Sendable, Identifiable {
    public let id: Int
    public let title: String
    public let body: String
}

public protocol HTTPSession: Sendable {
    func data(for request: URLRequest) async throws -> (Data, URLResponse)
}

extension URLSession: HTTPSession {
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {
        #if canImport(FoundationNetworking)
        // Linux FoundationNetworking async surface
        try await withCheckedThrowingContinuation { (cont: CheckedContinuation<(Data, URLResponse), Error>) in
            let task = self.dataTask(with: request) { data, response, error in
                if let error {
                    cont.resume(throwing: error)
                } else if let data, let response {
                    cont.resume(returning: (data, response))
                } else {
                    cont.resume(throwing: URLError(.badServerResponse))
                }
            }
            task.resume()
        }
        #else
        try await self.data(for: request)
        #endif
    }
}

public struct PostClient: Sendable {
    private let session: any HTTPSession
    private let baseURL: URL

    public init(session: any HTTPSession = URLSession.shared, baseURL: URL = URL(string: "https://jsonplaceholder.typicode.com")!) {
        self.session = session
        self.baseURL = baseURL
    }

// MARK: - TODO: Codable + URLSession
/*
 Goal:
 Fetch and decode an array of posts.

 Steps:
 1. Implement `fetchPosts()` using async/await.
 2. Build URL by appending path `posts`.
 3. Validate HTTP status 200..<300.
 4. Decode `[RemotePost]` with `JSONDecoder`.

 Hints:
 - Inject `HTTPSession` so tests can use a fake.
 - Do not invent custom JSON keys — models match the API.

 Acceptance criteria:
 - Returns non-empty posts from the public sample API when online.
 - Unit test uses fixture data without network.

 Docs:
 - https://developer.apple.com/documentation/foundation/urlsession
 - https://developer.apple.com/documentation/foundation/codable
 - https://developer.apple.com/documentation/foundation/jsondecoder
*/

    // public func fetchPosts() async throws -> [RemotePost] { fatalError("TODO") }
}

public struct FixtureSession: HTTPSession, Sendable {
    public var data: Data
    public var statusCode: Int
    public init(data: Data, statusCode: Int = 200) {
        self.data = data
        self.statusCode = statusCode
    }
    public func data(for request: URLRequest) async throws -> (Data, URLResponse) {
        let response = HTTPURLResponse(url: request.url!, statusCode: statusCode, httpVersion: nil, headerFields: nil)!
        return (data, response)
    }
}
