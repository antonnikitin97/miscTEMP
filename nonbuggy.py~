# Implemenation of a bubble sort.
# This code complies fine but has some errors that will prevent it
# from running properly.
# Find these errors and correct them, writing a comment explaining
# what the error was.


def sort_list(list_to_sort):
    temp_store = 0
    number_of_passes = len(list_to_sort) - 1    # - 1 Here to avoid list index out of bounds
    for i in range(number_of_passes):
        for i in range(len(list_to_sort) - 1):    # - 1 Here to avoid list index out of bounds
	    if list_to_sort[i] >= list_to_sort[i + 1]:
                temp_store_one = list_to_sort[i + 1]
                list_to_sort[i + 1] = list_to_sort[i]
                list_to_sort[i] = temp_store_one
    return list_to_sort


def print_contents(list_to_print):
    for i in list_to_print:
        print i

sorted_list = sort_list(list({3, 45, 212, 31, 53, 4}))
print_contents(sorted_list)

