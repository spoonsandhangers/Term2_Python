"""
insertion sort
"""
def insertionSort(myList):
	for i in range(1, len(myList)):

		indexValue = myList[i]
		indexPointer = i

		while indexPointer > 0 and myList[indexPointer-1] > indexValue:
			myList[indexPointer] = myList[indexPointer-1]
			indexPointer = indexPointer - 1

		myList[indexPointer] = indexValue

myList = [20, 11, 100, 45, 2, 54, 21, 78, 10, 55]
insertionSort(myList)
print(myList)



