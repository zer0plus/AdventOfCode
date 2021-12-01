rf = [int(rf) for rf in open("input.csv")]
last = None
curr = None
count = 0
for i, v in enumerate(rf):
    if i > 1:
        curr = rf[i-1] + rf[i-2] + v
        
    if curr is not None and last is not None:
        if curr > last:
            count += 1
    last = curr

print(count)