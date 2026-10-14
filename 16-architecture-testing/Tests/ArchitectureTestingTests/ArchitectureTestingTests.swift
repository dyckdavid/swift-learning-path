import Testing
@testable import ArchitectureTesting

@Test func repositoryStartsEmpty() async {
    let repo = InMemoryTodoRepository()
    #expect(await repo.all().isEmpty)
}

// @Test @MainActor func addAndToggle() async {
//     let vm = TodoViewModel(repository: InMemoryTodoRepository())
//     await vm.add(title: "Ship course")
//     #expect(vm.items.count == 1)
// }
