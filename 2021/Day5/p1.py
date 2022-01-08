import copy

read_file = [(read_file) for read_file in open("input.txt")]
read_trial = [(read_file) for read_file in open("trial.txt")]

def part1():
    cols = []
    for i in range(10*10):
        cols.append(0)
        # for j in range(10):
        #     row = {j : 0} # left side is x number and right side is how many times it has been crossed through
        #     cols.append({i: row}) # left side is y number and right side is the row in that y col with info on crossing
    # print(cols)
    def coord_to_index(x, y):
        return (x + (y*10))
    def index_to_coord(num):
        x = num % 10
        y = num // 10
        return x, y

    # print(index_to_coord(54))
    
    theBigList = []
    for i, v in enumerate(read_trial):
        striped = v.strip()
        start = striped.split("->")
        count = 0
        appender = []
        # print (start)
        for i, each in enumerate(start):
            coords = (each.split(","))
            appender.append(coords)
            count += 1
        copyee = copy.deepcopy(appender)
        theBigList.append(copyee)
        appender.clear()
    # print((theBigList))
    toAddX = []
    toAddY = []
    for i, coord in enumerate(theBigList):
        # print(coord)
        for j, xys in enumerate(coord):
            # print(xys)
            toAddX.append(int(xys[0]))
            toAddY.append(int(xys[1]))
        
        xDiff = int(toAddX[1]) - int(toAddX[0])
        yDiff = int(toAddY[1]) - int(toAddY[0])

        # print(xDiff) 
        # print(yDiff) 
        if xDiff > yDiff:
            # print(toAddX[0])
            # print(toAddX[1])
            # print("-----------")
            for hey in range(int(toAddY[0]), int(toAddY[1])):
                print(hey)
                for j in range(toAddX[0], toAddX[1]):
                    hah = coord_to_index(j, i)
                    cols[hah] += 1
        elif yDiff <= xDiff:
            # print(toAddX[0])
            # print(toAddX[1]) 
            # print("-----------")
            for hey in range(int(toAddX[0]), int(toAddX[1])):
                print(hey)
                for j in range(toAddY[0], toAddY[1]):
                    hah = coord_to_index(j, i)
                    cols[hah] += 1
                    

        toAddX.clear()
        toAddY.clear()
        # print(cols) 
        # cols[]
    return None

part1()