"""
Linear search
using subroutines with return values and parameters

"""

def inputNames():
	names = []
	for i in range(10):
		name = input("Enter a name: ")
		names.append(name)

	return names

def namesSearch(aList, item):
	for i in aList:
		if i == item:
			print("Name found!")
			return True
	return False

nameList = inputNames()
item = input("WHat name would you like to search for?")
found = namesSearch(nameList,item)
print("Found is set as:", found)

