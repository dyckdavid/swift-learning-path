import Testing
@testable import ProtocolsGenerics

@Test func storeStartsEmpty() {
    let store = MemoryStore<User>()
    #expect(store.all().isEmpty)
}
