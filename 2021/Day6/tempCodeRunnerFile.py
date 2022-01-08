ainDict[2]})
        mainDict.update({2: mainDict[3]})
        mainDict.update({3: mainDict[4]})
        mainDict.update({4: mainDict[5]})
        mainDict.update({5: mainDict[6]})
        mainDict.update({6: mainDict[7]})
        mainDict.update({7: mainDict[8]})
        if(mainDict[0] > 0):
            mainDict.update({8: (mainDict[0] + mainDict[8])})
            mainDict.update({0: mainDict[1]})
            print("mainDict") 
        else:
            mainDict.update({0: mainDict[1]})