import Testing
@testable import ArchitectureTesting

@Test func repositoryStartsEmpty() async {
    let repo = InMemoryTodoRepository()
    #expect(await repo.all().isEmpty)
}

@Test func addAndToggle() async {
    let vm = TodoViewModel(repository: InMemoryTodoRepository())
    await vm.add(title: "Ship course")
    #expect(vm.items.count == 1)
    let id = vm.items[0].id
    await vm.toggle(id: id)
    #expect(vm.items[0].isDone)
}
