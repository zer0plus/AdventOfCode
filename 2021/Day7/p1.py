import copy
trial_file = [(read_file) for read_file in open("trial.txt")]
input_file = [(read_file) for read_file in open("input.txt")]

for i, v in enumerate(input_file):
    inp = (v.strip().split(','))

maxNum = 0
minNum = 0
total = 0
for i, v in enumerate(inp):
    if (int(v)) > int(maxNum):
        maxNum = int(v)

add = 0
minAdd = len(inp)*maxNum
store = None
for i in range(minNum, maxNum+1):
    add = 0
    for j, v in enumerate(inp):
        add += abs(int(v) - i)
        
    if minAdd > add:
        minAdd = add
        store = i


print(minAdd)