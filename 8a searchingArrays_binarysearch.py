"""
A binary search finds the mid point of a sorted array
If the search value is less than the midpoint the lower part of the array is further examined
The midpoint of the lower part is then found and the same operation is carried out
this continues until the search term is found.

"""
import random

# list length is declared here as a global variable
# it's written in capitals as a python convention to show
# that it is a constant
LIST_LENGTH = 10

# This function takes a list length and
# a highest value and creates a random list
# of that length between 0 and the highest number
# No value will be repeated.
# This is not part of the search but helps when you are teaching as you
# can create lots of different lists very quickly
def random_num_list(list_length, highest_num):
    num_list = []
    index = 0

    while index < list_length:
        num = random.randint(1, highest_num)

        if not num in num_list:
            num_list.append(num)
            index += 1

    num_list.sort()
    return num_list

# a global variable my_list that uses the random_num_list
# function to create a list.
# The list is then printed
my_list = random_num_list(LIST_LENGTH, 20)
print(my_list)

# a binary search function that has 2 parameters
# the first parameter is the list to be searched
# the second parameter is the item to be searched for
def bin_search(alist, item):
	# first index is set at 0
	first_index = 0
	# last index is set at the list length
	# minus 1
	last_index = len(alist)-1
	#found equals false
	found = False

	#start of the search
	# the while loop condition is
	# first index is less than or equal to last index
	# found is not true
	while first_index <= last_index and not found:
		# find the midpoint index by using floor(integer) division to divide by 2
		midpoint = (first_index + last_index)//2

		print("The midpoint index is:", midpoint, "- The midpoint value is:", alist[midpoint] )

		# if the value at the midpoint index is equal to the item searched for
		# A message is printed
		# and true is returned
		if alist[midpoint] == item:
			print("Found it! At index:", midpoint)
			found = True
		# if item is not found we need to work out if the item is
		# less than or more than the value at the midpoint
		else:
			if item < alist[midpoint]:
				# if item is less than the midpoint
				# the last index is changed to the midpoint -1
				last_index = midpoint - 1
				print(alist[first_index:last_index])
			else:
				# if the item is more than the midpoint
				# the first item is changed to the first index + 1
				first_index = midpoint + 1
				print(alist[first_index:last_index])
		# The while loop runs again with the new pointer values
	#if the item is not found after the while loop has stopped the value
	# of found is still returned
	return found

# ask the user what number they would like to search for
my_num = int(input("what number would you like to search for: "))
print("Searching for number", my_num)
# start the binary search by passing the list and the number to the function.
bin_search(my_list, my_num)
