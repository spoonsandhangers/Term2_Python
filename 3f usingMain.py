"""
Now that the students understand what subroutines are
It will be useful to start using the main method.
Some programming languages like Java and C# have a dedicated main method (function)
This is always the starting point of the code.
Python does not specify this starting point but has coding conventions
That are followed to make sure programmers know where the code starts etc.
It is good practice to define a main() function and use it to call
the subroutines in your program and control the flow/sequence of the program.
Although you can import any module you have written you only want the main method
of the python file you are executing to run.
__name__ will be assigned a value depending on how the file is executed
if you are running the file from the command line or thonny __name__ will be
assigned the value __main__
If you have imported the file using an import statement __name__ will be given the
value of the name of the file.
This way the interpreter knows which file is being executed and which is being imported.
This code checks to see if this is the file being executed then starts by calling the main method.

All code should be contained in this way within a subroutine.
"""


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
