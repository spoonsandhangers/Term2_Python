"""
In python a list is the commonly used data structure.  This is similar to an array.
It is of variable length, changeable and indexed.
The index of a list begins at 0
Lists have lots of functions associated with them, some are very similar or the same as Strings
"""
# creating a list
# each element in a list is separated by a comma
# if they are strings they should have speech marks surrounding them
# Python even lets you combine different data types in a list see mixed data
houses = ["Hufflepuff", "Ravenclaw", "Slytherin", "Gryffindor"]
evenNums = [2, 4, 6, 8, 10]
mixedData = [1, "spoons", True, 34.8]

# print out an element of the list using it's index value
print(houses[1], "is the best house!\n")

# You can create a blank list and add to it later.
# when you add elements the list size will grow.
blankList = []

# use append() to add elements to the end of the list
blankList.append("newElement")
blankList.append("nextElement")

# any list index can be accessed directly by the index value
print("The element at index 0 is:", blankList[0], "\n")

# You can assign a value directly to an element within the list using the index number
# but only if that element already contains a value
blankList[0] = "assigned a new value"
print("The element at index 0 has now changed to:", blankList[0], "\n")

# if you try to assign a value or access a value at an index that has not
# been assigned a value already an error will be generated - IndexError
# I have used a try except block to catch this error here
try:
	blankList[3] = "this causes an error"
except IndexError:
	print("Index Error raised!")
	print("You tried to assign a value to an index that is out of range")
	print("You can only add or access elements upto and including the length of the list")
	print("\n")

# You can find out the length of a list in the same way
# you find the length of a string
length = len(houses)
print("The houses list is:", length, "Elements long\n")

# You can iterate through an array in the same ways you can iterate through a string
for i in houses:
	print(i)

print("")

for i in range(len(houses)):
	print(houses[i])

# You can split up a string by a specific character e.g. a comma or space
# and add each element to a list using the split function
# The code below produces a list of seasons using the string provided
myString = "winter,spring,summer,autumn"
stringList = myString.split(sep=',')
print(stringList)
