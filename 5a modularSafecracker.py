"""
Using functions and while loops
"""
import random # imports the random library

# set the safe code to "000"
safeCode = "000"

# define the functions that the menu will select.

# menu item 1 manually enter a 3 digit code
def enterCode():
	safeCode = input("Enter a 3-digit code for the safe: ")
	return safeCode

# menu item 2 randomlly generate a 3 digit code.
def randomCode():
	safeCode = random.randint(100,999)
	return safeCode

# menu item 5 create a loop for the user to guess
def guess():
	guess = True

	while guess:
		userGuess = input("Enter 3 digit code guess: ")
		if userGuess == safeCode:
			print("You guessed correctly!")
			guess = False
		else:
			print("Sorry guess again!")

# display the menu
def menu():
	print("\t1. Manually set a 3-digit safe code", "2. Randomly generate a 3-digit safe code", "3. Set max number of guesses", "4. Turn hints on/off", "5. Guess the code", "6. Exit",sep='\n\t')
	choice = input("Enter a number 1 to 5: ")
	return choice

# set play to true so that the loop will execute until play is set to false
play = True

while play:
	choice = menu()
	# each choice calls the appropriate sub routine
	if choice == "1":
		print("You have chosen option 1")
		safeCode = enterCode()

	elif choice == "2":
		print("You have chosen option 2")
		safeCode = randomCode()

	elif choice == "5":
		print("You have chosen option 5")
		guess()

	elif choice == "6":
		print("You have chosen option 6")
		play = False












