import argparse
import puzzleClass
from dfs_algorithm import dfs
from astar_algorithm import A_star
import time

def printResult(test, level, search):
    if level == 'all':
        for i in range(1, 41):
            print('Level: ' + str(i))
            test.readFile('./level/level'+str(i)+'.txt')
            test.print()
            result = None
            start = time.time()
            if (search == 'dfs'):
                result = dfs(test)
            else:
                result = A_star(test)

            if result == None:
                print("None!")
            else:
                print("%d steps" % len(result[0]))
                print(result[0])
                result[1].print()
            print("Time: %s" % (time.time() - start))
    else:
        print('Level: ' + level)
        test.readFile('./level/level'+level+'.txt')
        test.print()
        result = None
        start = time.time()
        if (search == 'dfs'):
            result = dfs(test)
        else:
            result = A_star(test)
        if result == None:
            print("None!")
        else:
            print("%d steps" % len(result[0]))
            print(result[0])
            result[1].print()
        print("Time: %s" % (time.time() - start))

if __name__ == '__main__':
    test = puzzleClass.Puzzle()

    parser = argparse.ArgumentParser('Choose searching method and level')
    parser.add_argument('-s', '--search', type=str, default='dfs', choices=['dfs', 'astar'],
                        help='Input searching method')
    parser.add_argument('-lv', '--level', default='all', help='Input level')
    args = parser.parse_args()

    if args.search == 'dfs':
        printResult(test, args.level, args.search)

    elif args.search == 'astar':
        printResult(test, args.level, args.search)

    else:
        print('Invalid searching method, please check it again')
