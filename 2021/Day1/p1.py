with open("input.csv", "r") as rf:
    count = 0
    for i, v in enumerate(rf.readlines()):
        
        if i != 0:
            if int(v) > last:
                # print(last) 
                count += 1
        last = int(v)
                
    print(count)