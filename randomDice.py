import random # import the random library

# rolls the dice 4 times and assigns each one to a different variable
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
roll4 = random.randint(1,6)

# Adds up all the roles.
totalRoll = roll1 + roll2 + roll3 + roll4

# Calculates the average of the rolls
# uses the round function to round to 2 decimal places.
averageRoll = round(totalRoll/4,2)

# prints out the result
print("The average roll is:", averageRoll)


