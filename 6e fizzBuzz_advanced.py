"""
Fizz buzz with more features
"""
#Global variables
maxNum = 100
fizz = 3
buzz = 5
fizzBuzz = 15

# replace all the hard coded numbers with the global variables
def fizzBuzzVariety():
	for i in range(1,maxNum+1):
		if i % fizzBuzz == 0:
			print("fizzBuzz")
		elif i % buzz == 0:
			print("Buzz")
		elif i % fizz == 0:
			print("Fizz")
		else:
			print(i)

def userChoices():
	maxNum = int(input("Enter an integer: "))
	buzz = int(input("Enter the buzz integer: "))
	fizz = int(input("Enter the fizz integer: "))
	fizzBuzz = int(input("Enter the fizzBuzz integer: "))
	return maxNum, buzz, fizz, fizzBuzz

# The return value for this function is 4 variables
# Python lets you set these variables using this syntax
# Other programming languages do not allow this
maxNum, buzz, fizz, fizzBuzz = userChoices()

#print out what the user has chosen
print("MaxNum is set at:", maxNum)
print("Buzz is set at:", buzz)
print("Fizz is set at:", fizz)
print("FizzBuzz is set at", fizzBuzz)

# run the fizz buzz subroutine.
fizzBuzzVariety()
