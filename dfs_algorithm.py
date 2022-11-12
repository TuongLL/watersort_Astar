from puzzleClass import Puzzle
import os
import psutil
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

# decorator function
def profile(func):
    def wrapper(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(
            func.__name__,
            mem_before, mem_after, mem_after - mem_before))
        return result
    return wrapper
@profile
def dfs(puzzle: Puzzle, attemp=100000):
    state_count = 0
    stack = []
    visited = set()
    stack.append(([], puzzle))
    visited.add(puzzle.convertToStr())
    while len(stack) > 0:
        path, pz = stack.pop(-1)
        visited.add(pz.convertToStr())
        if pz.stateChecking():
            print("%d states searched" % state_count)
            return path, pz
        for succ in pz.getSuccessors()[::-1]:
            act, suc_pz = succ
            if suc_pz.convertToStr() not in visited:
                stack.append((path.copy()+[act], suc_pz))
        state_count += 1
        if (state_count > attemp):
            print("Maximum number of times exceeded")
            return None
    print("Unsolvable")
    return None
