from puzzleClass import Puzzle 
def dfs(puzzle:Puzzle,attemp=100000):
    ttt = 0
    q = []
    visitted = set()
    q.append(([],puzzle))
    visitted.add(puzzle.convertToStr())
    while len(q)>0:
        path,pz = q.pop(-1)
        if pz.isRight():
            print("%d states searched"%ttt)
            return path,pz
        for succ in pz.get_successors():
            act,suc_pz = succ
            if suc_pz.convertToStr() not in visitted:
                q.append((path.copy()+[act],suc_pz))
                visitted.add(suc_pz.convertToStr())
        ttt += 1
        if (ttt>attemp):
            print("Maximum number of times exceeded")
            return None
    print("unsolvable")
    return None