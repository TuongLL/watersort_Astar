from puzzleClass import Puzzle


def bfs(puzzle: Puzzle, attemp=100000):
    ttt = 0
    q = []
    q.append(([], puzzle))
    while len(q) > 0:
        path, pz = q.pop(-1)
        if pz.isRight():
            print("%d states searched" % ttt)
            return path, pz
        for succ in pz.get_successors():
            act, suc_pz = succ
            q.append((path.copy()+[act], suc_pz))
        ttt += 1
        if (ttt > attemp):
            print("Maximum number of times exceeded")
            return None
    print("unsolvable")
    return None
