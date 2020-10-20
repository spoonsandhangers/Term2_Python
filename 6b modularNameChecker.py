"""
Solution to the standard challenge.
Where method is written change this to subroutine.
functions return a value procedures do not.
"""
# global variables
userName = ""

# a function to ask a user for their name
def setUserName():
	name = input("Enter your name: ")
	return name

# a procedure to iterate through the name and
# output print out each character
def checkUserName():
	for i in userName:
		if i.isalpha():
			print(i)


# Subroutine calls
userName = setUserName()
checkUserName()


