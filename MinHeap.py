# implement min_heap_sort

# takes an unordered list and returns a heap sorted list with minimum value at root

# careful to not alter the original list

# An unordered list to work with
# original_list = [10, 121, 94, 3, -7, 203, 45, 93, 27, -35, 6, 1, -7]


def parent_index(child_index):
	# For dense binary tree, returns index of parent associated with child_index

	return (child_index - 1) // 2



def swap_elements(array, index_1, index_2):
	# Question: will manipulations of array lead to a change in a more global variable. I think so- lists
	# 	are mutable

	array[index_1], array[index_2] = array[index_2], array[index_1]
	return array



def float_min_to_top(array):
	# Moves minimum element into the root position (index zero in the list)
	# The rest of the elements may be shuffled but this is not a min_heap, in general.

	for index in range(len(array)-1, 0, -1):
		parent = parent_index(index)
		if array[parent] > array[index]:
			swap_elements(array, index, parent)
	return array


def heap_sorted(array):
	answer = []
	for layer in range(len(array)-1, -1, -1):
		answer.append(float_min_to_top(array)[0])
		array[0] = array[len(array)-1]
		array.pop()

	return answer











