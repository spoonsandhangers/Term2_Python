"""
insertion lottery
"""
import random

def random_num_list(list_length, highest_num):
    num_list = []
    index = 0

    while index < list_length:
        num = random.randint(1, highest_num)

        if not num in num_list:
            num_list.append(num)
            index += 1

##    num_list.sort()
    return num_list

def insertionSort(myList):
	for i in range(1, len(myList)):

		indexValue = myList[i]
		indexPointer = i

		while indexPointer > 0 and myList[indexPointer-1] > indexValue:
			myList[indexPointer] = myList[indexPointer-1]
			indexPointer = indexPointer - 1

		myList[indexPointer] = indexValue


def checkTicket(aList,bList):
	matches = 0
	for i in aList:
		if i in bList:
			print("The number:", i, "is on your ticket")
			matches += 1
	return matches


ticket = random_num_list(6,49)
insertionSort(ticket)
print("The lottery ticket sorted is:", ticket)
lottery = random_num_list(6,49)
print("The lottery numbers are:", lottery)
matches = checkTicket(ticket,lottery)
print("You had", matches, "matching number(s)")


