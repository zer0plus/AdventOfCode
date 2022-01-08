    i, matrix, card = finder()
    totalNum = 0
    for i in matrix:
        print(i) 
        for valNum, val in enumerate(i):
            for k, v in val.items():
                if v == False:
                    totalNum += int(k)
    print(totalNum)
    print("card: " + str(card))