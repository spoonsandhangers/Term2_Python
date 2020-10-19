import random # imports the random library

# sets the variable play to an empty string
play = ""
# sets the user and computers scores to 0
scoreUser = 0
scoreComp = 0

# while the variable play does not equal the string "exit"
# Everything in the loop will run
# This will be tested each time the loop starts again.
while play != "exit":
	# asks the user to input either rock paper or scissors
	# converts that to lower case.
	userChoice = input("Enter your choice 'rock', 'paper' or 'scissors': ").lower()

	# assigns the computer a choice of 1,2 or 3 randomly
	compChoice = random.randint(1,3)

	# works out which choice the computer has made
	# 1 = rock, 2 = paper, 3 = scissors.
	if compChoice == 1:
		compChoice = 'rock'
	elif compChoice == 2:
		compChoice = 'paper'
	elif compChoice == 3:
		compChoice = 'scissors'

	# prints out each choice
	print("You have chosen:", userChoice)
	print("The computer has chosen:", compChoice)

	# Tests if it is a draw
	# Then goes through each userChoice
	# each choice has a nested part that runs if it is chosen.
	# The nested part tests the computer choice compared to the user choice
	# To see who will win.
	# The else condition runs if the user has not entered one of the choices.

	# Each time the user or computer wins the variable that stores their score is
	# incremented by 1
	if userChoice == compChoice:
		print("It's a draw!")
	elif userChoice == "rock":
		if compChoice == "paper":
			print("Computer Wins!")
			scoreComp += 1
		elif compChoice == "scissors":
			print("Player wins!")
			scoreUser += 1
	elif userChoice == "paper":
		if compChoice == "rock":
			print("Player wins!")
			scoreUser += 1
		elif compChoice == "scissors":
			print("Computer wins!")
			scoreComp += 1
	elif userChoice == "scissors":
		if compChoice == "rock":
			print("Computer wins!")
			scoreComp += 1
		elif compChoice == "paper":
			print("Player wins!")
			scoreUser += 1
	else:
		print("You haven't chosen from rock, paper or scissors! Computer wins!")
		scoreComp += 1

	# prints out the scores of the computer and the player at the end of this round.
	print("Player score:", scoreUser)
	print("Computer score:", scoreComp)

	# Asks the user if they want to exit
	# assigns the user input to the variable play
	# this will now be tested by the while loop
	# to see if the game continues.
	play = input("Type 'exit' to finish game or press enter to continue: ")


