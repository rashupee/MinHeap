# Heap sort algorithm practice. I learned a little more how to code up an interesting algorithm.
# This algorithm is based upon a data structure called a heap which is similar to a binary tree.
# This code does not quite generate min heaps. The root is smaller than its children after a call
# of the function float_min_to_top on a list, but the pattern does not in general happen lower
# than root.


def parent_index(child_index):
	# For dense binary tree, returns index of parent associated with child_index. Dense means there are
	# no empty nodes between the root and the last element.

	return (child_index - 1) // 2



def swap_elements(array, index_1, index_2):
	# Takes an array and swaps the elements.

	array[index_1], array[index_2] = array[index_2], array[index_1]
	
	return array



def float_min_to_top(array):
	# Moves minimum element into the root position (index zero in the list)
	# This function does not fully sort the array in that all children are not necessarily
	# larger than their parents- only true for the root node and its children.

	for index in range(len(array)-1, 0, -1):
		parent = parent_index(index)
		if array[parent] > array[index]:
			swap_elements(array, index, parent)

	return array



def heap_sorted(array):
	# Generates answer which is a sorted version of the given array. Original array is not changed.
	# Follows the algorithm which moves the smallest element to the root, puts this element in the answer list
	# replaces this with the last element of the unsorted array, and repeats for every element in the unsorted
	# list.

	array_copy = [element for element in array]
	answer = []
	for layer in range(len(array_copy)-1, -1, -1):
		answer.append(float_min_to_top(array_copy)[0])
		array_copy[0] = array_copy[len(array_copy)-1] # Move last element of left over array to the root node
		array_copy.pop() 

	return answer











