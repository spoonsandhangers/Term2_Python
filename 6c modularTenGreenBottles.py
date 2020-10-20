"""
Change method to subroutine in this question.
I haven't completed the bottles of beer challenge
It's the same but with different words and a higher range value.

"""
# the range values in this loop count down from 10
# start postion is 10, end position is 0, step value is -1
def greenBottles():
	for i in range(10,0,-1):
		print(i, "green bottles left hanging on the wall")

# subroutine call
greenBottles()

print("\n\n End of first part \n\n")

#import time module
import time

def greenBottlesDelay():
	for i in range(10,0,-1):
		print(i, "green bottles left hanging on the wall")
		time.sleep(1) # pauses for 1 second.

#subroutine call
greenBottlesDelay()

