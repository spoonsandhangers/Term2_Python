"""
Fizz buzz challenge
change the word method to subroutine.
There are a few ways to do this challenge

"""
# This solution uses a nested if statement
# if i mod 5 = 0 it then tests to see if i mod 3 is also 0 this is a fizzbuzz
def fizzBuzz1():
	for i in range(1,101):
		if i % 5 == 0:
			if i % 3 == 0:
				print("FizzBuzz")
			else:
				print("Buzz")
		elif i % 3 == 0:
			print("Fizz")
		else:
			print(i)

# this subroutine uses mod 15 first to test for fizz buzzes
# then mod 5 then mod 3.
def fizzBuzz2():
	for i in range(1,101):
		if i % 15 == 0:
			print("fizzBuzz")
		elif i % 5 == 0:
			print("Buzz")
		elif i % 3 == 0:
			print("Fizz")
		else:
			print(i)

fizzBuzz1()
fizzBuzz2()


