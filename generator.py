import random

cup_num = int(input("Number of cups:"))
capacity = int(input("Cup capacity:"))
empty_cup = int(input("Number of empty cups:"))
state = []
for i in range(cup_num):
    if i < empty_cup:
        state.append([])
    else:
        state.append([i]*capacity)
path = []
N = 100
for step in range(N):
    i = random.randint(0,cup_num-1)
    while len(state[i])==0:
        i = random.randint(0,cup_num-1)
    j = random.randint(0,cup_num-1)
    while j == i or len(state[j]) == capacity:
        j = random.randint(0,cup_num-1)
    state[j].append(state[i].pop())
    path.append((j,i))
for i in range(empty_cup):
    while len(state[i])!=0:
        j = random.randint(empty_cup,cup_num-1)
        while j == i or len(state[j]) == capacity:
            j = random.randint(empty_cup,cup_num-1)
        state[j].append(state[i].pop())
        path.append((j,i))
print(state)
with open("p.txt",'w') as f:
    f.writelines([str(cup_num)+'\n',str(capacity)+'\n'])
    sss = []
    for cup in state:
        a = ""
        for w in cup:
            a += str(w)+" "
        sss.append(a+'\n')
    f.writelines(sss)