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
        try await withCheckedThrowingContinuation { (cont: CheckedContinuation<(Data, URLResponse), Error>) in
            let task = self.dataTask(with: request) { data, response, error in
                if let error { cont.resume(throwing: error) }
                else if let data, let response { cont.resume(returning: (data, response)) }
                else { cont.resume(throwing: URLError(.badServerResponse)) }
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

    public func fetchPosts() async throws -> [RemotePost] {
        let url = baseURL.appendingPathComponent("posts")
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        let (data, response) = try await session.data(for: request)
        guard let http = response as? HTTPURLResponse, (200..<300).contains(http.statusCode) else {
            throw URLError(.badServerResponse)
        }
        return try JSONDecoder().decode([RemotePost].self, from: data)
    }
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
