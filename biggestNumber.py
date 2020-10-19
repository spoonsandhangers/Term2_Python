# Ask the user for 2 numbers and cast them to ints

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# tests which number is greater, if neither is greater they must be the same.
if num1 > num2:
	print("The largest number is number 1:", num1)
elif num2 > num1:
	print("The largest number is number 2:", num2)
else:
	print("The numbers are the same!")

# tests which out of three numbers is largest
num3 = int(input("Enter a third number: "))

# if num1 is larger than num2
# we write another if statement nested inside the first
# This statement only runs if num1 is larger than num2
# it tests whether num1 is larger than num3.

# if num1 is not larger than num2 then it moves on to the next elif statement
# this tests if num2 is more than num3
# then next elif statement tests if num3 is larger than num2

# if none of these conditions equate to true the else statement runs
# All the numbers must then be the same.
if num1 > num2:
	if num1 > num3:
		print("The largest number is number 1:", num1)
	else:
		print("The largest number is number 3", num3)
elif num2 > num3:
	print("The largest number is number 2:", num2)
elif num3 > num2:
	print("The largest number is number 3:", num3)
else:
	print("The 3 numbers are equal.")


