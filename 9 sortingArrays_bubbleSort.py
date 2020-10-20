"""
sorting arrays

"""
import time
import random

start = time.time()

LIST_LENGTH = 15

def random_num_list(list_length, highest_num):
    num_list = []
    index = 0

    while index < list_length:
        num = random.randint(1, highest_num)

        if not num in num_list:
            num_list.append(num)
            index += 1

##    num_list.sort()
    return num_list

my_list = random_num_list(LIST_LENGTH, 25)
print(my_list)

def bubble_sort(alist):
    for i in range(len(alist)):
        print("Pass number {} ".format(i+1))

        for j in range(len(alist)-1):

            if alist[j] > alist[j+1]:
                print("swapping...{} and {} ".format(alist[j], alist[j+1]))
                temp = alist[j+1]
                alist[j+1] = alist[j]
                alist[j] = temp
                print(alist)

finished_list = bubble_sort(my_list)
print('')
print(finished_list)
print('')

end = time.time()
print("Time taken to run bubble sort is:")
print(end - start)
