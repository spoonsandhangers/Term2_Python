"""
For loops are called count controlled iteration
Unlike while loops that are controlled by a condition
for loops run a certain number of times and then stop.
The i variable after the key word for is the loop variable
Each time the loop executes the loop variable is incremented
The value of the loop variable starts at 0
You can only use the loop variable inside the loop (local variable)
The loop variable does not need to be called i.  You can call it anything you like.
It is convention to call it i and if using a nested loop j
"""

print("\n\nFirst for loop\n")
# prints out "I love loops" 10 times
for i in range(10):
	print("I love loops")

print("\n\nSecond for loop\n")
# prints out the value of the loop variable i on each loop
# notice that this starts at 0
for i in range(10):
	print(i)

print("\n\nThird for loop\n")
# prints out the value of the loop variable i in the range 1 to 10
# The second element is the stop value and is value minus 1.
for i in range(1,11):
	print(i)

print("\n\nfourth for loop\n")
# prints out the even values of the loop variable i in the range 2 to 10
# This uses the third element of the range function which is the step
# In this case step is set to 2
for i in range(2,11,2):
	print(i)


print("\n\nfifth for loop\n")
# Asks the user for the number of the multiplication table to print
# Uses a for loop to print out that table
# Note the use of i the loop variable
multiplier = int(input("Enter the multiplication table you want to print: "))

for i in range(1,13):
	print(i, "X", multiplier, "=", multiplier * i)


print("\n\nfifth for loop\n")
# using the keyword break terminates a loop immediately.
