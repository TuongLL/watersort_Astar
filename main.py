import puzzleClass
from bfs_algorithm import bfs
from astar_algorithm import A_star
test = puzzleClass.Puzzle()
for i in range(1,41):
    print('Level: ' + str(i))
    test.ereadfile('./level/level'+str(i)+'.txt')
    test.print()
    # a = A_star(test)
    a = bfs(test)
    if a == None:
        print("None!")
    else:
        print("%d steps"%len(a[0]))
        print(a[0])
        a[1].print()