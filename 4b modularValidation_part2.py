"""
Change the functions so instead of using the global variables
the functions ask the user for the input that needs to be validated.
"""

# create a presence check function that asks for user input
def presenceCheck():
	userName = input("Enter a user name: ")
	if len(userName) == 0:
		print("Error Presence Check: user name is empty")
	else:
		print("User name OK")

# create a length check function that asks for user input
def lengthCheck():
	password = input("Enter a password: ")
	if len(password) < 8:
		print("Error length check:  Password is too short")
	else:
		print("Password length OK")

# create a range check function that asks for user input
def rangeCheck():
	testScore = int(input("Enter a test score: "))
	if testScore < 0 or testScore > 100:
		print("Error range check: test score is out of range")
	else:
		print("Test score range OK")


#function calls
presenceCheck()
lengthCheck()
rangeCheck()
