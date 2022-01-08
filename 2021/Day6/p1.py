# import copy

# with open("trial.txt", "r") as rf:
#     arr = []
#     for i, v in enumerate(rf.readline()):
#         # print(v)
#         if v != ",":
#             arr.append(int(v))
#     # print(arr)

#     mainArr = []
#     for i in range(8):
#         mainArr.append(0)

#     for i, v in enumerate(arr):
#         mainArr[v] += 1
#     # print(mainArr)
#     temp = 0
#     for x in range(18):
#         for i, v in enumerate(reversed(mainArr)):
#             if i == 7:
#                 if v > 0:
#                     mainArr[7] += v
#                     mainArr[0] = 0
            
#             elif i > 0 and i < 7:
#                 temp2 = copy.deepcopy(mainArr[i])
#                 mainArr[i] = temp
#                 temp = copy.deepcopy(temp2)
#                 # print(temp)


#             elif i == 0:
#                 temp = copy.deepcopy(v)
#             print(mainArr)


            
#             # print(i)

#         # print(x)

#     # print(mainArr)

#     # mainDict = {
#     #     0: 0,
#     #     1: 0,
#     #     2: 0,
#     #     3: 0,
#     #     4: 0,
#     #     5: 0,
#     #     6: 0,
#     #     7: 0,
#     #     8: 0
#     # }
#     # for j, v in enumerate(arr):
#     #     mainDict[v] += 1
#     # keys = list(mainDict.keys())
#     # values = list(mainDict.values())

#     # for i in range(18):
#     #     # for j in range(len(keys)):
#     #         # print(mainDict[1])
#     #         # print(mainDict[2])
#     #         # print(mainDict[4])
#     #         # print(mainDict[3])
#     #         # print(mainDict[5])
#     #     mainDict.update({1: mainDict[2]})
#     #     mainDict.update({2: mainDict[3]})
#     #     mainDict.update({3: mainDict[4]})
#     #     mainDict.update({4: mainDict[5]})
#     #     mainDict.update({5: mainDict[6]})
#     #     mainDict.update({6: mainDict[7]}) 
#     #     mainDict.update({7: mainDict[8]})
#     #     if(mainDict[0] > 0):
#     #         mainDict.update({8: (mainDict[0] + mainDict[8])})
#     #         mainDict.update({0: mainDict[1]})
#     #         print("mainDict") 
#     #     else:
#     #         mainDict.update({0: mainDict[1]})


#     #             # mainDict.update({keys[i]: 0})
#     #         # mainDict[0] = int(mainDict[1])
#     #         # mainDict[1] = mainDict[2]
#     #         # mainDict[2] = mainDict[3]
#     #         # mainDict[3] = mainDict[4]
#     #         # mainDict[4] = mainDict[5]
#     #         # mainDict[5] = mainDict[6]
#     #         # mainDict[6] = mainDict[7]
#     #         # mainDict[7] = mainDict[8] 
            
#     #             # mainDict[8] += mainDict[0]
#     #             # mainDict = 0
#     # print(mainDict) 

fish = [[int(f) for f in open("trial.txt").read().split(',')].count(i) for i in range(9)]
print(fish)
for i in range(90): 
    fish.append(fish.pop(0))
    fish[6] += fish[8]
print(sum(fish))