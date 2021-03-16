def binary_search_recursive (sorted_array, element):
	step_middle = (len(sorted_array) - 1) // 2
	if len(sorted_array) == 1:
		if sorted_array[0] == element:
			return 0
		else:
			return -1
	elif sorted_array[step_middle] >= element:
		solution_in_next_step = binary_search_recursive(sorted_array[:step_middle + 1], element)
		if solution_in_next_step >= 0:
			return solution_in_next_step
		else:
			return -1
	else: # elif sorted_array[step_middle] < element:
		solution_in_next_step = binary_search_recursive(sorted_array[step_middle + 1:], element)
		if solution_in_next_step >= 0:
			return step_middle + 1 + solution_in_next_step
		else:
			return -1

def binary_search_iterative(sorted_array, element):
	index = 0
	step_length = len(sorted_array)
	while step_length >= 1:
		#print((index, step_length, sorted_array[index + step_length]))
		while index + step_length < len(sorted_array) and sorted_array[index + step_length] < element:
			index += step_length
		step_length //= 2
	
	# Pre

	if index == 0:
		if sorted_array[0] == element:
			return 0
		else:
			return -1
	elif sorted_array[index] == element:
		return index
	elif sorted_array[index + 1] == element:
		return index + 1
	else:
		return -1

	# New

	if sorted_array[index] == element:
		return index
	elif sorted_array[index + 1] == element:
		return index + 1
	else:
		return -1