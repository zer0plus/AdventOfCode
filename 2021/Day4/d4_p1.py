import copy

# from d4_p2 import main
with open("input.txt") as rf:
    count = 0
    matrixList = []
    matrixBox = []
    for i, v in enumerate(rf.readlines()):
        
        if i == 0:
            firstLine = v.strip()
            cardList = firstLine.split(",")
            # print(cardList)
        elif count > 0:
            matrixLine = v.strip()
            matrixListRow = matrixLine.split(" ")
            for k, l in enumerate(matrixListRow):
                if l == "":
                    matrixListRow.pop(k)
            for i, v in enumerate(matrixListRow):
                matrixListRow[int(i)] = {v: False}
            matrixBox.append(matrixListRow)
            # print(matrixListRow)
            if count == 5:
                appendBox = copy.deepcopy(matrixBox)
                # print(matrixBox)
                matrixList.append(appendBox)
                matrixBox.clear()
                count = 0
            else:
                count += 1
        else:
            count += 1

    def finder():
        # print(matrixList)
        
        ##### Above Completes the process of forming the data structure for the cards and the matrixes

        ###Below I am going to iterate through each card and turn the corresponding values to light up
        hor = False
        # hor= False
        for cardNum, card in enumerate(cardList):
            hor = False
            for matrixNum, matrixs in enumerate(matrixList): # Goes through all matrixes
                trueCountVertical1 = 0
                trueCountVertical2 = 0
                trueCountVertical3 = 0
                trueCountVertical4 = 0
                trueCountVertical5 = 0
                for rowNum, rows in enumerate(matrixs): # Goes through 5 rows each box
                    trueCountHorizontal = 0
                    for valueNum, values in enumerate(rows): # Goes through 5 values each row
                        if card in values.keys():
                            values[(card)] = True
                            trueCountHorizontal += 1
                            if valueNum == 0:
                                trueCountVertical1 += 1
                            if valueNum == 1:
                                trueCountVertical2 += 1
                            if valueNum == 2:
                                trueCountVertical3 += 1
                            if valueNum == 3:
                                trueCountVertical4 += 1
                            if valueNum == 4:
                                trueCountVertical5 += 1
                        else:
                            for i in values.values():
                                if i == True:
                                    trueCountHorizontal += 1
                                    if valueNum == 0:
                                        trueCountVertical1 += 1
                                    if valueNum == 1:
                                        trueCountVertical2 += 1
                                    if valueNum == 2:
                                        trueCountVertical3 += 1
                                    if valueNum == 3:
                                        trueCountVertical4 += 1
                                    if valueNum == 4:
                                        trueCountVertical5 += 1
                        if trueCountHorizontal > 4:
                            return matrixNum, matrixs, card
                            # hor = True
                            # trueCountHorizontal = 0
                            # print("matrixs5")
                            # break
                        elif (trueCountVertical1 > 4 or trueCountVertical2 > 4 or trueCountVertical3 > 4 or trueCountVertical4 > 4 or trueCountVertical5 > 4):
                            return matrixNum, matrixs, card
                            # hor= True
                            # print("matrixs6")
                            # trueCountVertical1 = 0
                            # trueCountVertical2 = 0
                            # trueCountVertical3 = 0
                            # trueCountVertical4 = 0
                            # trueCountVertical5 = 0
                            # break
                    # if (trueCountVertical1 > 4 or trueCountVertical2 > 4 or trueCountVertical3 > 4 or trueCountVertical4 > 4 or trueCountVertical5 > 4):
                    #         hor= True
                    #         trueCountVertical1 = 0
                    #         trueCountVertical2 = 0
                    #         trueCountVertical3 = 0
                    #         trueCountVertical4 = 0
                    #         trueCountVertical5 = 0
                    #         print("matrixs4")
                    #         break
            #         if(hor is True):
            #             print("matrixs3")
            #             break
            #     if(hor is True):
            #         print("matrixs2")
            #         break
            # if(hor is True):
            #     print("matrixs1")
            #     totalNum = 0
            #     for i in matrixs:
            #         print(i) 
            #         for valNum, val in enumerate(i):
            #             for k, v in val.items():
            #                 if v == False:
            #                     totalNum += int(k)
            #     print(totalNum)
            #     print("card: " + str(card))

            #     matrixList.pop(matrixNum)


                # break
                    
        # print(matrixList)
        
    while len(matrixList) > 0:
        i, matrix, card = finder()
        matrixList.pop(i)


    totalNum = 0
    for i in matrix: 
        print(i) 
        for valNum, val in enumerate(i):
            for k, v in val.items():
                if v == False:
                    totalNum += int(k)
    print(totalNum)
    print("card: " + str(card))