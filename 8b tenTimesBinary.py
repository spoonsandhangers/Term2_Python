"""
binary search
"""

def makeList():
	myList = []
	for i in range(100):
		myList.append(i*10)
	return myList

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


aList = makeList()
print(aList)
found = bin_search(aList,350)
print("found is set to:", found)
found = bin_search(aList,750)
print("found is set to:", found)
