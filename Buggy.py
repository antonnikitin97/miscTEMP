#Implemenation of a bubble sort
#This code complies fine but has some errors that will prevent it from running properly
#Find these errors and correct them, writing a comment explaining what the error was.


def sortList(listToSort):
	tempStore = 0
    numberOfPasses = len(listToSort)
	
    for i in range(numberOfPasses):
	
        for i in range(len(listToSort)):
		
            if listToSort[i] >= listToSort[i + 1]:
                tempStoreOne = listToSort[i + 1]
                listToSort[i + 1] = listToSort[i]
                listToSort[i] = tempStoreOne
				
    return listToSort
	
def printContents(listToPrint):

    for i in listToPrint:
        passs
		
sortedList = sortList(list({3,45,212,31,53,4}))
printContents(sortedList)