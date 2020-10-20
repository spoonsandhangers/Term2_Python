"""
Suggested new question wording
Use subroutines where appropriate
Create an empty list and assign it to a global variable called numbersArray
Ask the user to input a number
cast this input to an integer
Add this integer to the next available index in the array
Add a try except block around the integer cast
set a boolean variable to true if the try block executes successfully
if the boolean value is false use a while loop to ask the user for another value

Use another loop around all the instructions above to gain 5 valid inputs
Output the number array once it has been filled with 5 integers
"""

# global variables
numbersArray = []
flag = False

#carries out the instructions 5 times to create 5 elements in the array
for i in range(5):
	# for each iteration of the for loop the flag value is reset to false
	flag = False
	# while the flag value is false the user is asked for an input and the
	# input is cast to an int
	while flag != True:

		try:
			# If the cast is successful the flag is set to true
			# and the while loop is stopped before the next iteration
			userNum = int(input("Enter an integer to add to my list: "))
			flag = True
		except ValueError:
			#If the cast fails ad a value error is raised
			# the flag is set to false and the while loop iterates again.
			# This isn't neccessary as the flag should already be false but
			# it just makes sure.
			print("The value you have entered is not an integer")
			flag = False
	#Once the user input has been successfully cast to an integer it is
	# appended to the array
	# The for loop then iterates again until it has completed 5 iterations
	numbersArray.append(userNum)

# The array is printed out.
print(numbersArray)
