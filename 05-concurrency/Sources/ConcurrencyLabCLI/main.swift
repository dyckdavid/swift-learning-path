import ConcurrencyLab

let board = ScoreBoard()
await board.setScore(10, for: "David")
print(await board.score(for: "David") ?? -1)
