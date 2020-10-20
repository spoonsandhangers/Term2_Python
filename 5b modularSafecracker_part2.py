"""
Using functions and while loops complete menu
"""
import random # imports the random library

# set the safe code to "000"
safeCode = "000"
maxGuesses = 1000
hintsON = False

# define the functions that the menu will select.

# menu item 1 manually enter a 3 digit code and return it so it can be assigned to the global variable safeCode
def enterCode():
	safeCode = input("Enter a 3-digit code for the safe: ")
	return safeCode

# menu item 2 randomly generate a 3 digit code and return it so it can be assigned to the global variable safeCode
def randomCode():
	safeCode = random.randint(100,999)
	return safeCode

# Set maximum guesses and return the number so that it can be assigned to the global variable.
def setMaxGuess():
	guessNumber = int(input("Enter the max number of guesses"))
	return guessNumber

# turns hints on or off.  Returns the value true or false to be assigned to the global variable hintsON
def hints():
	hints = input("Enter 'on' or 'off' for hints: ")
	if hints == 'on':
		return True
	elif hints == 'off':
		return False
	else:
		print("Hints not set as input incorrect")

# menu item 5 create a loop for the user to guess
def guess():
	# guess is set to true and guesses to 0
	guess = True
	guesses = 0

	# while loop runs while guess is true and guesses is less than maxGuesses
	while guess and guesses < maxGuesses:
		# asks the user for their guess
		userGuess = input("Enter 3 digit code guess: ")
		#if the user guess is equal to the safe code
		# guess is set equal to false to break the loop
		if userGuess == safeCode:
			print("You guessed correctly!")
			guess = False
		# else if hints are on the user is told which digits they guessed correctly
		else:
			if hintsON:
				if safeCode[0] == userGuess[0]:
					print("HINT:")
					print("You got the first digit correct.")
				if safeCode[1] == userGuess[1]:
					print("HINT:")
					print("You got the second digit correct.")
				if safeCode[2] == userGuess[2]:
					print("HINT:")
					print("You got the third digit correct.")
			# this code runs even if hints are off
			# guesses is incremented to prevent an infinite loop
			# A message is printed telling the user how many guesses they have had.
			print("Sorry guess again!")
			guesses += 1
			print("Number of Guesses taken:", guesses)

# display the menu as a bulleted list
# validate the input with a try except block
# if it is not an integer an error will occur and the menu will be reloaded using menu()
def menu():
	print("\t1. Manually set a 3-digit safe code", "2. Randomly generate a 3-digit safe code", "3. Set max number of guesses", "4. Turn hints on/off", "5. Guess the code", "6. Exit",sep='\n\t')
	try:
		choice = int(input("Enter a number 1 to 5: "))
		return choice
	except ValueError:
		print("The value you hae entered is not a digit.")
		menu()

# set play to true so that the loop will execute until play is set to false
play = True

# This while loop executes all the code
# I would usually put all this in a main() method but this is long enough without adding any more code.
while play:
	choice = menu()
	# each choice calls the appropriate sub routine
	if choice == 1:
		print("You have chosen option 1")
		safeCode = enterCode()

	elif choice == 2:
		print("You have chosen option 2")
		safeCode = randomCode()

	elif choice == 3:
		print("You have chosen option 3")
		maxGuesses = setMaxGuess()
		print("Max guesses is set at:", maxGuesses)

	elif choice == 4:
		print("You have chosen option 4")
		hintsON = hints()
		print("Hints on is now:",hintsON)

	elif choice == 5:
		print("You have chosen option 5")
		guess()

	elif choice == 6:
		print("You have chosen option 6")
		play = False












