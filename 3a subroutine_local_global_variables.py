"""
A variable is a space in memory, that stores a value, that can change while the program is running.
variables that are declared inside subroutines are called local variables.
variables that are declared outside of subroutines are called global variables.
This is called a variables scope.
"""
# In this subroutine the variable subject is local.
# You can only use this inside this subroutine

def studySubject():
	subject = input("Enter the subject you study: ")
	print("I love", subject, "!")


# subroutine call
studySubject()


#######################################################################
# this subroutine asks the user for a number
# stores this number in a variable userNum
# multiplies the variable by 2 and stores it in the variable userNumTwice
# prints out userNumTwice.


def numDoubled():
	userNum = int(input("Enter a number: "))
	userNumTwice = userNum * 2
	print(userNumTwice)



numDoubled()

#####################################################################
# Here a global variable called num is declared outside any subroutine
# assigned the value 500
num = 500

# This subroutine is created, it contains a local variable called num
# This is assigned the value 10
def localNumber():
	num = 10
	print("Local num", num)

# This prints out the global variable 500
print("Global num", num)
# The global variable is incremented by 1 to make it 501
num += 1
print("Global num", num)

# The subroutine localNumber is called and prints out the local variable num
# Which is equal to 10
localNumber()

# The global variable num still equals 501.
print("Global num", num)


# As Java is an OOP language the approach in the book is OOP from an early stage.
# I have not taken this route yet as they haven't learned about OOP and won't until after christmas.
# This is an extra file to try to explain scope a little more than the book does.



