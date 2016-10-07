#Implemenation of a bubble sort
tempStoreOne = 0
def sortList(listToSort):
    # Total passes = length of list - 1
    numberOfPasses = len(listToSort)
    for i in range(numberOfPasses):
        # This will cause an indexArrayOutOfBounds (need to minus 1 from the length)
        for i in range(len(listToSort)):
            # Should be > and not >=
            if listToSort[i] >= listToSort[i + 1]:
                tempStoreOne = listToSort[i + 1]
                listToSort[i + 1] = listToSort[i]
                listToSort[i] = tempStoreOne
    return listToSort
def printContents(listToPrint):
    for i in listToPrint:
        print i
sortedList = sortList(list({3,45,212,31,53,4}))
printContents(sortedList)