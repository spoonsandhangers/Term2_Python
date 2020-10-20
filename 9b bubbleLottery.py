"""
bubble lottery
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

def highestNum(aList):
	highNum = aList[0]

	for i in range(len(aList)):
		if highNum < aList[i]:
			highNum = aList[i]
	return highNum

def lowestNum(aList):
	lowNum = aList[0]

	for i in range(len(aList)):
		if lowNum > aList[i]:
			lowNum = aList[i]
	return lowNum

def bubble_sort(alist):
    for i in range(len(alist)):
        print("Pass number {} ".format(i+1))

        for j in range(len(alist)-1):

            if alist[j] > alist[j+1]:
                print("swapping...{} and {} ".format(alist[j], alist[j+1]))
                temp = alist[j+1]
                alist[j+1] = alist[j]
                alist[j] = temp
                print(alist)

ticket = random_num_list(6,49)
highestValue = highestNum(ticket)
lowestValue = lowestNum(ticket)
print("ticket numbers:", ticket)
print("The highest number on the ticket is:", highestValue)
print("The lowest number on the ticket is:", lowestValue)
bubble_sort(ticket)
print("Sorted ticket:", ticket)

