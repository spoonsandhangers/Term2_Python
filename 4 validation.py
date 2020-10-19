"""
Validation methods
I've put these inside functions to make it tidy but you
can just use the inside of the function if you want to with the
corresponding variable.
This would mean taking away the return values e.g.

name = ""

if name == "":
	print("Presence error: Name is blank")
else:
	print("Name ok")

"""
# Global variables
name = ""
phone = "0798734580"
deposit = 200
email = "studentcollege.com"
age = "twenty"
year = "Year 12"

# All functions return True if the value is valid
# and false if the value is invalid.
# They also print out a message to tell the user the result.
def presenceCheck():
	if len(name) == 0:
		print("Name is blank")
		return False
	else:
		print("Name is OK")
		return True

def lengthCheck():
	if len(phone) == 11:
		print("Phone number is correct length")
		return True
	elif len(phone) > 11:
		print("Length Error: Phone number is too long")
		return False
	else:
		print("Length Error: Phone number is too short")
		return False

def rangeCheck():
	if deposit > 0 and deposit < 1000:
		print("Deposit is within range")
		return True
	else:
		print("Range error: Deposit out of range")
		return False

def formatCheck():
	if "@" in email:
		print("Email OK")
		return True
	else:
		print("Format error: Email has no @")
		return False

def typeCheck():
	try:
		userage = int(age)
		print("Age is a valid data type")
		return True
	except ValueError:
		print("A value error has occurred")
		print("The value you entered for age was not a number")
		return False


def lookupCheck():
	if year == "AS" or year == "A2":
		print("Valid year selected from list")
		return True
	else:
		print("Lookup Error: Value not in list")
		return False

def main():
	# All the functions are called here
	# The return value is set to a variable
	# This value is a boolean true or false.

	nameOK = presenceCheck()
	lengthOK = lengthCheck()
	rangeOK = rangeCheck()
	formatOK = formatCheck()
	ageOK = typeCheck()
	yearOK = lookupCheck()

	# the if statement checks if all the conditions are met.
	# if they are each value will be true

	if nameOK and lengthOK and rangeOK and formatOK and ageOK and yearOK:
		print("All values are valid")
	else:
		print("There is at least one validation error")










if __name__ == "__main__":
	main()
