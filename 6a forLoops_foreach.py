"""
For loops can be used to iterate through lists/arrays and strings (a string is a special type of list)
We haven't covered lists/arrays yet so I will stick to strings.
You can still use the range function to iterate through a string.
Sometimes this is preferable
"""
print("\n\nFirst for loop\n")
# declare a variable myString
myString = "iteration"
# Iterate through the string using a for loop
# here letter is the loop variable
# I could change that to i or anything I wanted.
for letter in myString:
	print(letter)


print("\n\nSecond for loop\n")
# This is the same as the for loop above just using the range function
# and accessing the string directly
for letter in range(len(myString)):
	print(myString[letter])


print("\n\nthird for loop\n")
for letter in myString:
	print(letter * 5, ".............")


print("\n\nfourth for loop\n")
# using the keyword break terminates a loop immediately.
myString = "catastrophe"
# using a for loop to find the letter s in the string myString and then stop
for i in range(len(myString)):
	if myString[i] == "s":
		print("s has been found on loop number:", i+1)
		break
	else:
		print("Loop number:", i+1 , "Letter:", myString[i])




