import random # you have to import the random library to use any random function.

# A random integer between 0 and 100 (inclusive) is generated
# This number is assigned to the variable myNum.
myNum = random.randint(0,100)

print(myNum)

# A random integer between 0 and 3 (inclusive) is generated
# This number is assigned to the variable myNum1
myNum1 = random.randrange(4)

print(myNum1)

# The following are a selection of more advanced random functions
# Just in case you want to use them.

# randrange can be given up to 3 numerical parameters.
# The first is the start integer, the second is the stop integer, the third is the step.
# 0,8,2 will choose between 0, 2, 4 and 6
# 1,4 will choose between 1, 2 and 3
myNum2 = random.randrange(0,8,2)

print(myNum2)

# choice selects a single element from a list.
# This is then assigned to the variable myChoice.
myChoice = random.choice(["rock", "paper", "scissors"])

print(myChoice)

# sample takes a list and a k value.
# It returns a list k long which is a random sample of the list without replacement.
# without replacement means that values will only appear in the sample once.
myList = [2,4,6,8,10,12,14,16]

mySample = random.sample(myList, k=3)

print(mySample)
print(myList)

