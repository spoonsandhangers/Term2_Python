import random  # imports the random library

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
if userChoice == compChoice:
	print("It's a draw!")
elif userChoice == "rock":
	if compChoice == "paper":
		print("Computer Wins!")
	elif compChoice == "scissors":
		print("Player wins!")
elif userChoice == "paper":
	if compChoice == "rock":
		print("Player wins!")
	elif compChoice == "scissors":
		print("Computer wins!")
elif userChoice == "scissors":
	if compChoice == "rock":
		print("Computer wins!")
	elif compChoice == "paper":
		print("Player wins!")
else:
	print("You haven't chosen from rock, paper or scissors! Computer wins!")



