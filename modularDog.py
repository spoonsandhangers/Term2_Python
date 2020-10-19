# dog name procedure.
def dogName():
	name = input("Enter a name for your dog: ")
	print("your dog is called", name)

# subroutine call
dogName()

def coatColour():
	colour = input("Enter the coat colour of your dog: ")
	print("your dog's coat colour is", colour)


def eyeColour():
	colour = input("Enter the eye colour of your dog: ")
	print("Your dog's eye colour is", colour)


def lengthCM():
	length = input("Enter the length of your dog in cm: ")
	print("Your dog's length is", length, "cm")


def weightKG():
	weight = input("Enter the weight of your dog in KG: ")
	print("Your dog's weight is", weight, "KG")

def price():
	price = input("Enter the price of your dog in pence: ")
	print("Your dog cost", price, "pence")

# function calls
coatColour()
eyeColour()
lengthCM()
weightKG()
price()

# a command for your dog
def dogCommand():
	print("Please enter either 'sit' or 'speak'")
	dogCom = input("Enter a command for your dog: ")
	if dogCom == 'sit':
		print("Your dog is sitting with it's tail wagging!")
	elif dogCom == 'speak':
		print("Woof woof!")
	else:
		print("Sorry your dog doesn't understand that command.")

dogCommand()
