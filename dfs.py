def dfs(puzzle: Puzzle, attempt=10000):
    puzzle_count = 0  # Count the number of reached states
    puzzle_stack = []
    puzzle_stack.append(([], puzzle))
    while len(puzzle_stack) > 0:
        path, pz = puzzle_stack.pop(-1)
        if pz.isComplete():
            print("%d states reached" % puzzle_count)
            return path, pz
        for suc in pz.getSuccessors():
            act, state = suc
            puzzle_stack.append((path.copy()+[act], state))

        puzzle_count += 1
        if (puzzle_count > attempt):
            print("Maximun number of times exceeded")
            return None

    print("Unsolvable")
    return None
