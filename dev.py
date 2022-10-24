import copy
from queue import PriorityQueue
class Puzzle(object):
    def __init__(self,cup_num=0,capacity=0) -> None:
        self.cup_num = cup_num #Number of cups
        self.capacity = capacity #Cup capacity
        self.empty_cup = 0
        self.state = None

    def create(self):
    	# Input status
        self.cup_num = int(input("Number of cups:"))
        self.capacity = int(input("Cup capacity:"))
        cup_num  = self.cup_num
        capacity = self.capacity
        self.state = []
        for i in range(cup_num):
        	# Space separation color
        	# The cup is empty
            water = input("The first%d A cup(From bottom to top): "%i).split()[:capacity]
            if len(water) == 0:
                self.empty_cup += 1
            self.state.append(water)
        return self.state
    def ereadfile(self,file):
    	# Read status from file
        with open(file,'r') as f:
            self.cup_num = int(f.readline())
            self.capacity = int(f.readline())
            self.state = []
            for i in range(self.cup_num):
                water = f.readline().split()[:self.capacity]
                if len(water) == 0:
                    self.empty_cup += 1
                self.state.append(water)
        return self.state
    def get_successors(self):
    	# Get all subsequent States and actions
        suc = []
        for i in range(self.cup_num):
            for j in range(self.cup_num):
                if self.isAction((j,i)):
                    suc.append(((j,i),self.move((j,i))))
        return suc
    def isAction(self,act:tuple,state=None):
    	# Judge whether it is a legal action
        # from j to i
        j,i = act
        if state == None:
            state = self.state
        return i!=j and len(state[j])>0 and len(state[i])<self.capacity and (len(state[i])==0 or state[j][-1]==state[i][-1])
        # Two different cups and the original cup is not empty and the target cup is not full (the target cup is empty or the top color is the same)
    def move(self,act:tuple):
    	# Act on the current state and generate a new state
        j,i = act
        state = copy.deepcopy(self.state)
        while self.isAction(act,state):
            state[i].append(state[j].pop()) 
            # Move one piece of water at a time instead of one share
        new_puzzle = Puzzle(self.cup_num,self.capacity)
        new_puzzle.empty_cup = self.empty_cup
        new_puzzle.state = state
        return new_puzzle
    def isRight(self)->bool:
    	# Is the target state
        if self.state is None:
            return False
        for i in range(self.cup_num):
            if len(self.state[i]) != 0 and len(self.state[i]) != self.capacity:
                return False
            elif len(self.state[i]) == self.capacity:
                for j in range(1,self.capacity):
                    if self.state[i][j] != self.state[i][0]:
                        return False
        return True
    def print(self,cup_width=6, cup_interval=3):
    	# Print current status
        if self.state is None:
            print(None)
            return None
        width = cup_width
        interval = cup_interval
        space = " "*interval
        a = ""
        for i in range(self.cup_num):
            a += ("#%d"%i).center(width+2)+space
        print(a)
        print()
        for j in range(self.capacity-1,-1,-1):
            a = ""
            for i in range(self.cup_num):
                if len(self.state[i]) > j:
                    color = self.state[i][j]
                else:
                    color = "."
                a += "|"+("%s"%color).center(width)+"|"+space
            print(a)
        a = ""
        for i in range(self.cup_num):
            a += "\\"+"_".center(width,"_")+"/"+space
        print(a)
        return None
    def A_star_cost(self)->int:
        #smaller is better
        # Acceptable and consistent heuristics
        step = 0
        bottom = {}
        for cup in self.state:
            if len(cup)==0:
                continue
            bottom[cup[0]] = bottom.get(cup[0],-1) + 1
            first_color = cup[0]
            all_same = 0
            for i in range(1,len(cup)):
                if cup[i] != first_color:
                    first_color = cup[i]
                    step += 1
                    all_same = 1
            if all_same == 0 and len(cup) == self.capacity:
                step -= 1
            if all_same == 0 and len(cup) < self.capacity and bottom[cup[0]]>=1:
                step += 1
        step += sum(bottom.values())
        return step

def heuristic_function(path, suc_pz):
    return len(path)+suc_pz.A_star_cost()
def validate_path(path):
    return (path[-1][1] == path[-2][0] and path[-1][0] == path[-2][1])
def A_star(puzzle:Puzzle,attemp=100000):
    ttt = 0
    q = PriorityQueue()
    q.put((puzzle.A_star_cost(),[],puzzle))
    print(puzzle.A_star_cost())
    while not q.empty():
        score,path,pz = q.get()
        if pz.isRight():
            print("%d states searched"%ttt)
            return path,pz
        if len(path)<2 or (len(path)>=2 and not validate_path(path)):
            for succ in pz.get_successors():
                act,suc_pz = succ
                q.put((heuristic_function(path, suc_pz),path.copy()+[act],suc_pz))
        ttt += 1
        if (ttt>attemp):
            print("Maximum number of times exceeded")
            return None
    print("unsolvable")
    return None
test = Puzzle()
# test.create()
test.ereadfile("89.txt")
test.print()
a = A_star(test)

if a == None:
    print("None!")
else:
    print("%d steps"%len(a[0]))
    print(a[0])
    a[1].print()