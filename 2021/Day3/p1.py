import copy
read_file = [(read_file) for read_file in open("input.txt")]

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
# d6 = []
# d7 = []
# d8 = []
# d9 = []
# d10 = []
# d11 = []
# d12 = []

f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
# f6 = []
# f7 = []
# f8 = []
# f9 = []
# f10 = []
# f11 = []
# f12 = []

dave = copy.deepcopy(read_file)
steve = copy.deepcopy(read_file)

def makeCols():
    d1.clear()
    d2.clear()
    d3.clear()
    d4.clear()
    d5.clear()
    # d6.clear() 
    # d7.clear()
    # d8.clear()
    # d9.clear()
    # d10.clear()
    # d11.clear()
    # d12.clear()
    for i, v in enumerate(dave):
        count = 0
        for j in v:
            count += 1
            if count == 1:
                d1.append(j)
            elif count == 2:
                d2.append(j)
            elif count == 3:
                d3.append(j)
            elif count == 4:
                d4.append(j)
            elif count == 5:
                d5.append(j)
            # elif count == 6:
            #     d6.append(j)
            # elif count == 7:
            #     d7.append(j)
            # elif count == 8:
            #     d8.append(j)
            # elif count == 9:
            #     d9.append(j)
            # elif count == 10:
            #     d10.append(j)
            # elif count == 11:
            #     d11.append(j)
            # elif count == 12:
            #     d12.append(j)


def makeColsTwo():
    f1.clear()
    f2.clear()
    f3.clear()
    f4.clear()
    f5.clear()
    # f6.clear() 
    # f7.clear()
    # f8.clear()
    # f9.clear()
    # f10.clear()
    # f11.clear()
    # f12.clear()
    for i, v in enumerate(steve):
        count = 0
        for j in v:
            count += 1
            if count == 1:
                f1.append(j)
            elif count == 2:
                f2.append(j)
            elif count == 3:
                f3.append(j)
            elif count == 4:
                f4.append(j)
            elif count == 5:
                f5.append(j)
            # elif count == 6:
            #     f6.append(j)
            # elif count == 7:
            #     f7.append(j)
            # elif count == 8:
            #     f8.append(j)
            # elif count == 9:
            #     f9.append(j)
            # elif count == 10:
            #     f10.append(j)
            # elif count == 11:
            #     f11.append(j)
            # elif count == 12:
            #     f12.append(j)

makeCols()
makeColsTwo()

# sigma = ''
# beta = ''

# zeroCount = 0
# oneCount = 0
# for i in d1: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'


# zeroCount = 0
# oneCount = 0
# for i in d2: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d3: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d4: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d5: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d6: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d7: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d8: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d9: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d10: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d11: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'

# zeroCount = 0
# oneCount = 0
# for i in d12: 
#     if i == '0':
#         zeroCount += 1
#     if i == '1':
#         oneCount += 1
# if zeroCount > oneCount:
#     sigma += '0'
#     beta += '1'
# else:
#     sigma += '1'
#     beta += '0'
# # print(sigma)
# # print(beta)




def part2Oxygen(dave):

    while(len(dave) > 1):

        zeroCount = 0
        oneCount = 0
        for i in d1: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[0] == '1':
                    dave.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[0] == '0':
                    dave.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[0] == '0':
                    dave.pop(i)
                else:
                    continue
        makeCols()

        zeroCount = 0
        oneCount = 0
        for i in d2: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[1] == '1':
                    dave.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[1] == '0':
                    dave.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[1] == '0':
                    dave.pop(i)
                else:
                    continue
        makeCols()

        zeroCount = 0
        oneCount = 0
        for i in d3: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[2] == '1':
                    dave.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[2] == '0':
                    dave.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[2] == '0':
                    dave.pop(i)
                else:
                    continue
        makeCols()

        zeroCount = 0
        oneCount = 0
        for i in d4: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[3] == '1':
                    dave.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[3] == '0':
                    dave.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[3] == '0':
                    dave.pop(i)
                else:
                    continue
        makeCols()

        zeroCount = 0
        oneCount = 0
        for i in d5: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[4] == '1':
                    dave.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[4] == '0':
                    dave.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(dave):
                if(len(dave) < 2):
                    break
                if v[4] == '0':
                    dave.pop(i)
                else:
                    continue
        makeCols()
        

        # zeroCount = 0
        # oneCount = 0
        # for i in d6: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[5] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[5] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[5] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d7: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[6] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[6] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[6] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d8: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[7] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[7] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[7] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d9: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[8] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[8] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[8] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d10: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[9] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[9] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[9] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d11: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[10] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[10] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[10] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

        # zeroCount = 0
        # oneCount = 0
        # for i in d12: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[11] == '1':
        #             dave.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[11] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(dave):
        #         if(len(dave) < 2):
        #             break
        #         if v[11] == '0':
        #             dave.pop(i)
        #         else:
        #             continue
        # makeCols()

    print(dave)

# rf = [(rf) for rf in open("input.txt")]

def part2Carbon(steve):

    while(len(steve) > 1):
        zeroCount = 0
        oneCount = 0
        for i in f1: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[0] == '0':
                    steve.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[0] == '1':
                    steve.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[0] == '1':
                    steve.pop(i)
                else:
                    continue
        makeColsTwo()

        zeroCount = 0
        oneCount = 0
        for i in f2: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[1] == '0':
                    steve.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[1] == '1':
                    steve.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[1] == '1':
                    steve.pop(i)
                else:
                    continue
        makeColsTwo()

        zeroCount = 0
        oneCount = 0
        for i in f3: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[2] == '0':
                    steve.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[2] == '1':
                    steve.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[2] == '1':
                    steve.pop(i)
                else:
                    continue
        makeColsTwo()

        zeroCount = 0
        oneCount = 0
        for i in f4: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[3] == '0':
                    steve.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[3] == '1':
                    steve.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[3] == '1':
                    steve.pop(i)
                else:
                    continue
        makeColsTwo()

        zeroCount = 0
        oneCount = 0
        for i in f5: 
            if i == '0':
                zeroCount += 1
            if i == '1':
                oneCount += 1
        if zeroCount > oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[4] == '0':
                    steve.pop(i)
                else:
                    continue
        elif zeroCount == oneCount:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[4] == '1':
                    steve.pop(i)
                else:
                    continue
        else:
            for i, v in enumerate(steve):
                if(len(steve) < 2):
                    break
                if v[4] == '1':
                    steve.pop(i)
                else:
                    continue
        makeColsTwo()
        

        # zeroCount = 0
        # oneCount = 0
        # for i in f6: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[5] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[5] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[5] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f7: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[6] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[6] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[6] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f8: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[7] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[7] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[7] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f9: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[8] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[8] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[8] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f10: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[9] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[9] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[9] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f11: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[10] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[10] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[10] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

        # zeroCount = 0
        # oneCount = 0
        # for i in f12: 
        #     if i == '0':
        #         zeroCount += 1
        #     if i == '1':
        #         oneCount += 1
        # if zeroCount > oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[11] == '0':
        #             steve.pop(i)
        #         else:
        #             continue
        # elif zeroCount == oneCount:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[11] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # else:
        #     for i, v in enumerate(steve):
        #         if(len(steve) < 2):
        #             break
        #         if v[11] == '1':
        #             steve.pop(i)
        #         else:
        #             continue
        # makeColsTwo()

    print(steve)


part2Oxygen(dave)
part2Carbon(steve)