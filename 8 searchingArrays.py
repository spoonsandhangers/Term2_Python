"""
To search a list you need a list and a value to search for.
You can declare these as global variables
Or you could use parameters with your subroutines.
A parameter is a value that you pass to a subroutine.
Parameters go inside the brackets that follow a subroutine call.
Your subroutine must specify that a value will be passed to it when it is defined using the def key word.
A value must be added inside those brackets too.
See example for better explanation.
"""
# example using linear search and global variables
# values are examined one after the other until the value is found
# global variables
myList = ["cats", "sleep", "anywhere"]
searchTerm = "anywhere"

def searchList():
	for i in myList:
		if i == searchTerm:
			return True
	return False

found = searchList()
print("The result of the search is:", found)


# example using linear search and a parameter for search term
# global variable for list
myList2 = ["Mo", "Bobby", "Virgil", "Sadio"]

def searchList2(term):
	for i in myList2:
		if i == term:
			return True
	return False

found = searchList2("Mo")
print("The result of search2 is:",found)


