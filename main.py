import argparse
import puzzleClass
from dfs_algorithm import dfs
from astar_algorithm import A_star

def printResult(test, level, result):
    if level == 'all':
        for i in range(1,41):
            print('Level: ' + str(i))
            test.readFile('./level/level'+str(i)+'.txt')
            test.print()
            if result == None:
                print("None!")
            else:
                print("%d steps" % len(result[0]))
                print(result[0])
                result[1].print()

    else:
        print('Level: ' + level)
        test.readFile('./level/level'+level+'.txt')
        test.print()
        if result == None:
            print("None!")
        else:
            print("%d steps" % len(result[0]))
            print(result[0])
            result[1].print()

if __name__ == '__main__':
    test = puzzleClass.Puzzle()

    parser = argparse.ArgumentParser('Choose searching method and level')
    parser.add_argument('--search', type=str, default='dfs',
                        help='Input searching method')
    parser.add_argument('--level', default='all', help='Input level')
    args = parser.parse_args()

    if args.search == 'dfs':
        result = dfs(test)
        printResult(test, args.level, result)

    elif args.search == 'astar':
        result = A_star(test)
        printResult(test, args.level, result)

    else: 
        print('Invalid searching method, please check it again')

    # if args.level == 'all':
    #     for i in range(1, 41):
    #         print('Level: ' + str(i))
    #         test.readFile('./level/level'+str(i)+'.txt')
    #         test.print()
    #         if (args.search == 'dfs'):
    #             result = dfs(test)
    #             if result == None:
    #                 print("None!")
    #             else:
    #                 print("%d steps" % len(result[0]))
    #                 print(result[0])
    #                 result[1].print()

    #         if (args.search == 'astar'):
    #             result = A_star(test)
    #             if result == None:
    #                 print("None!")
    #             else:
    #                 print("%d steps" % len(result[0]))
    #                 print(result[0])
    #                 result[1].print()
    #         else:
    #             print("Invalid searching method, please check it again!")
