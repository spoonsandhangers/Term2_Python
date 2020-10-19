""" A subroutine is a re-useable piece of code that can be called anytime during the program
In Java everything is object oriented so the Java book calls them methods.
It is best to call them subroutines before we cover OOP theory.
Subroutines can be split into 2 groups procedures and functions.
Procedures do not return a value explicitly.
Functions return a value using a return statement.
The subroutines used here will all be procedures."""

# subroutines in Python all start with the keyword def
# The interpreter reads the subroutines but does not execute them
# Until they are called.
# Everything contained inside a subroutine is indented.


def sayHello():
	print("Hello!")


def sayGoodbye():
	print("Goodbye!")


def subjects():
	print("I study:")
	print("\t* Computer Science.")
	print("\t* Maths.")
	print("\t* Physics.")

# These are subroutine calls
# The name of the subroutine followed by an open then a closed bracket.
sayHello()
subjects()
sayGoodbye()


