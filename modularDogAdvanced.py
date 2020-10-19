"""
The original task for this is an OOP task.
To change it to subroutines it requires knowledge of functions which are subroutines
that return a value.

"""
# Global Variables
dogName = "bob"
eyeColour = "blue"
dogCoat = "brown"
lengthCM = 50
weightKG = 20
pricePennies = 500
menu = True

# subroutines now return the new value to the subroutine call
# All variables contained in the subroutines are local.
def dogName():
	name = input("Enter your new dog name: ")
	return name


def coatColour():
	colour = input("Enter the new coat colour of your dog: ")
	return colour


def eyeColour():
	colour = input("Enter the new eye colour of your dog: ")
	return colour


def lengthCM():
	length = input("Enter the new length of your dog in cm: ")
	return length


def weightKG():
	weight = input("Enter the new weight of your dog in KG: ")
	return weight

def price():
	price = input("Enter the new price of your dog in pence: ")
	return price

# while the variable menu is true the while loop will keep running.
while menu:
	# ask the user to enter a number that will be used to choose a subroutine
	print("Please enter a number to select an attribute to change:")
	print("\t1. Name", "2. Coat colour", "3. Eye colour", "4. length in cm", "5. Weight in KG", "6. Price in pence", "7. Exit", sep='\n\t')
	choice = input("Enter a number: ")
	# the value of choice is tested to see what subroutine to call
	if choice == "1":
		# The variable dogName is a global variable
		# The return value from the subroutine dogName() is assigned to
		# this global variable.
		# Without this variable assignment the return value would be lost.
		dogName = dogName()
		print("Your new dog name is", dogName)
	elif choice == "2":
		dogCoat = coatColour()
		print("Your dog's new coat colour is", dogCoat)
	elif choice == "3":
		eyeColour = eyeColour()
		print("Your dog's new eye colour is", eyeColour)
	elif choice == "4":
		lengthCM = lengthCM()
		print("Your dog's new length is", lengthCM)
	elif choice == "5":
		weightKG = weightKG()
		print("Your dog's new weight is", weightKG)
	elif choice == "6":
		pricePennies = price()
		print("Your dog's new price is", pricePennies)
	elif choice == "7":
		menu = False
	else:
		print("You have not entered an acceptable number.")




