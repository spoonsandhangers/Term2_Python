"""
I have added this section, without learning OOP this is the way that we can
show how to use global and local variables.
Updating global variables in this way will lead into using OOP instance variables and methods.
Subroutines that return a value are called functions
They use the key word return
To use the return value you must assign it to a variable.
"""

# Global variables
name = "bob"
subject = "Computer Science"
group = "15AA"

def updateName():
	name = input("Enter the new name: ")
	return name

def updateSubject():
	subject = input("Enter the new subject: ")
	return subject

def updateGroup():
	group = input("Enter the new subject: ")
	return group

# Print out the original name
print("Your name is:", name)
# use the updateName subroutine to assign a new value to the variable name
name = updateName()
#print out the updated name
print("Your updated name is:", name)

# update the subject
print("Your subject is:", subject)
subject = updateSubject()
print("Your updated subject is:", subject)

# update the group
print("Your group is:", group)
group = updateGroup()
print("Your updated group is:", group)

