"""
Removing the OOP references from the advanced task.
Continue adding validation functions

Create a lookup function that asks for user input
Create a type check function for an integer that asks for user input
Create a format check function to check that a time has a : in it.  This should also ask for user input.

"""

# Create a look up check that takes user input
def lookupCheck():
	userName = input("Enter your user name: ")
	if userName == "admin" or userName == "bob":
		print("Valid user name selected from list")
	else:
		print("Lookup Error: Value not in list")

# Create a type check that takes user input
def typeCheck():
	try:
		height = input("Enter your height in CM")
		height = int(height)
		print("Height is a valid data type")

	except ValueError:
		print("A value error has occurred")
		print("The value you entered for height was not a number")

#create a format check that asks for a user input
def formatCheck():
	time = input("Enter the time in the format xx:xx ")
	if ":" in time:
		print("Time OK")

	else:
		print("Format error: Time has no :")

# function calls
lookupCheck()
typeCheck()
formatCheck()
