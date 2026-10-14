import Testing
@testable import ConcurrencyLab

@Test func fakeFetchReturnsLength() async {
    let result = await AsyncExercises.fakeFetch(id: "abcd")
    #expect(result.value == 4)
}
