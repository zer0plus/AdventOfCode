fish = [[int(f) for f in open("input.txt").read().split(',')].count(i) for i in range(9)]
print(fish)
for i in range(256): 
    fish.append(fish.pop(0))
    fish[6] += fish[8]
print(sum(fish))