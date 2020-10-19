import random # import the random library

# Set card1 and card2 to random integers between 1 and 11 inclusive.
card1 = random.randint(1,11)
card2 = random.randint(1,11)

# print out the values of the players cards
print("player card 1: ", card1)
print("player card 2: ", card2)

# Add together the players cards
cardTotal = card1 + card2

# Print out the total of the players cards
print("Player card total:", cardTotal)

# if the players card total is not equal to 21 ask the player
# if they want to stick or twist 's' or 't'.
# this has an else statement on the same indent
# for when the players total is 21.
if cardTotal != 21:
	# add .lower() at the end of the input request to convert the input to
	# lower case
	userChoice = input("Would you like to twist 't' or stick 's'? ").lower()

	# if the player chooses 't' randomly select another card for them.
	if userChoice == "t":
		card3 = random.randint(1,11)
		print("player card 3:", card3)
		# Add this new card to the total
		cardTotal += card3
		print("player new total:", cardTotal)

	# if the players card total is less than 21
	# This if statement has an elif and else on the same indent.
	# The elif checks to see if the player has 21
	# the else then runs if the player hasn't got 21 or less than 21.
	# As they must be bust.
	if cardTotal < 21:
		# set dealerCard1 and 2 to random numbers between 1 and 11 inclusive
		dealerCard1 = random.randint(1,11)
		dealerCard2 = random.randint(1,11)

		# print out these numbers.
		print("Dealer card 1:", dealerCard1)
		print("Dealer card 2:", dealerCard2)

		# Add up the values of the two cards
		dealerTotal = dealerCard1 + dealerCard2

		print("Dealer card total:", dealerTotal)

		# if the dealers total is less than or equal to 17
		# automatically deal them another card.
		if dealerTotal <= 17:
			dealerCard3 = random.randint(1,11)

			# Add this card to the dealers total.
			dealerTotal += dealerCard3

			print("Dealers hand is less than 17 so they receive an extra card:", dealerCard3)
			print("Dealer total now:", dealerTotal)

		# these selection statements decide whether the dealer has 21
		# if the dealer has more than 21 so is bust
		# if the dealers total is more than the players.
		if dealerTotal == 21:
			print("Dealer wins with 21!")
		elif dealerTotal > 21:
			print("Player wins, dealer is bust!")
		elif dealerTotal >= cardTotal:
			print("Dealer wins with:", dealerTotal)
		else:
			print("Player wins with:", cardTotal)

	elif cardTotal == 21:
		print("BlackJack! Well done player wins!")
	else:
		print("Dealer wins player is bust!")
else:
	print("BlackJack! Well done player wins!")
