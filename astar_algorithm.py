from queue import PriorityQueue
from puzzleClass import Puzzle
from memory_profiler import profile
@profile

def h_n(puzzle: Puzzle) -> int:
    # Smaller is better
    # Acceptable and consistent heuristics
    step = 0
    bottom = {}
    for cup in puzzle.state:
        if len(cup) == 0:
            continue
        bottom[cup[0]] = bottom.get(cup[0], -1) + 1
        first_color = cup[0]
        all_same = True
        for i in range(1, len(cup)):
            if cup[i] != first_color:
                first_color = cup[i]
                step += 1
                all_same = False
        if all_same and len(cup) == puzzle.capacity:
            step -= 1
    step += sum(bottom.values())
    return step


def g_n(path):
    return len(path)


def f_n(path, puzzle):
    return g_n(path) + h_n(puzzle)


def visited_state(visited, pz):
    return pz.convertToStr() in visited


def A_star(puzzle: Puzzle, attemp=100000):
    state_count = 0
    q = PriorityQueue()
    q.put((h_n(puzzle), [], puzzle))
    visited = set()
    visited.add(puzzle.convertToStr())
    while not q.empty():
        score, path, pz = q.get()
        if pz.stateChecking():
            print("%d states searched" % state_count)
            return path, pz
        if len(path) < 2 or (len(path) >= 2 and not visited_state(visited, pz)):
            for succ in pz.getSuccessors():
                act, suc_pz = succ
                q.put((f_n(path+[act], suc_pz), path.copy()+[act], suc_pz))
        state_count += 1
        visited.add(pz.convertToStr())
        if (state_count > attemp):
            print("Maximum number of times exceeded")
            return None
    print("Unsolvable")
    return None
