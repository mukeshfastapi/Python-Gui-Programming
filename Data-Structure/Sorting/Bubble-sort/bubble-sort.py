# Programme to implementing bubble sort algorithm

def bubblesort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1],customList[j]

    print(customList)


clist = [4, 1, 3, 9, 8, 5, 7]

bubblesort(clist)



