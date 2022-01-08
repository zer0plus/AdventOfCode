import copy

def coolAddition(int_n):
    total = 0
    for i in range(int_n):
        total += i + 1
    return(total)
# print(coolAddition(9))

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

part2_add = 0
minAdd = (len(inp)*(coolAddition(maxNum)))
store = None 
for i in range(minNum, maxNum+1):
    part2_add = 0
    for j, v in enumerate(inp):
        part2_add += coolAddition(abs(int(v) - i))
            
    if minAdd > part2_add:
        minAdd = part2_add
        store = i

print(store)
print(minAdd)