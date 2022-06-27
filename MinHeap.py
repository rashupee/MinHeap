# implement min_heap_sort

# takes an unordered list and returns a heap sorted list with minimum value at root

# careful to not alter the original list

original_list = [10, 121, 94, 3, -7, 203, 45, 93, 27, -35, 6, 1, -7]

min_heap = []


def swap_elements(array, index_1, index_2):
	# Question: will manipulations of array lead to a change in a more global variable. I think so- lists
	# 	are mutable

	high, low = max(index_1, index_2), min(index_1, index_2)

	array.insert( low, array.pop( high ))
	array.insert( high, array.pop( low + 1 ))

	return array




