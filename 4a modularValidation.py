"""
Again I have changed this to be a challenge about functions instead of
OOP so where it talks about declaring an object, this won't be the case.

new problem:

Declare 3 global variables that you can validate using 3 functions:
1. Presence check
2. Length check with a lower limit.
3. Range check with an upper and lower limit

Create the 3 functions
validate the variables.

Change the functions so instead of using the global variables
the functions ask the user for the input that needs to be validated. (see 4b)

Carry out tests to make sure your functions work over a range of values.
"""
# Global variables
userName = ""
password = "12345"
testScore = 123

# create a presence check function
def presenceCheck():
	if len(userName) == 0:
		print("Error Presence Check: user name is empty")
	else:
		print("User name OK")

# create a length check function
def lengthCheck():
	if len(password) < 8:
		print("Error length check:  Password is too short")
	else:
		print("Password length OK")

# create a range check function.
def rangeCheck():
	if testScore < 0 or testScore > 100:
		print("Error range check: test score is out of range")
	else:
		print("Test score range OK")


#function calls
presenceCheck()
lengthCheck()
rangeCheck()


