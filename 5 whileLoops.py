"""
While loops are called condition controlled iteration.
The condition is tested before the loop executes.
This means that the loop may never execute if the condition is false at the start.
Each time the loop has executed the condition is re checked before the next iteration.

It is important that you use a variable to control the loop so that the condition can
eventually become false and you don't end up with an infinite loop.
"""
import time

# using an integer variable to control the loop
count = 0

while count < 10:
	print(count)
	# incrementing the count variable by 1 each time
	# prevents the loop being infinite
	# as it means that it will eventually be more than 10
	count += 1

# using boolean flag value to control the loop
# This is often used as a game loop
# To run until game over or until the user exits.
stopFlag = True

while stopFlag:
	print("Looping")
	#use the time function to pause the loop for 5 seconds
	time.sleep(5)
	# after 5 seconds set the stopFLag to false to exit the loop
	stopFlag = False

print("Exited the loop after 5 seconds")

# using a break statement will exit the loop even if the condition
# is still true
stopFlag = True

while stopFlag:
	print("Looping")
	time.sleep(2)
	break

print("Exited the loop after a break statement")
print("stop flag is still set as: ", stopFlag)




