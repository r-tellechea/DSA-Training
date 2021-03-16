class Permutation ():
	def __init__(self, order):
		# Introduce the permutation order
		self.size = len(order)
		self.order = []
		for element in order:
			self.order.append(element)
		
		# Update the permutation code
		self.array_code = []
		for index in range(self.size - 1):
			number_of_minor_elements = 0
			for subarray_index in range(index, self.size):
				if self.order[index] > self.order[subarray_index]:
					number_of_minor_elements += 1
			self.array_code.append(number_of_minor_elements)
		
	def __str__(self):
		permutation_string = "("
		for element in self.order:
			permutation_string += f"{str(element)}, "
		return permutation_string[:-2] + ")"

	def __lq__(self, other):
		for index in range(self.size - 1):
			if self.order[index] < other.order[index]:
				return True
			elif self.order[index] > other.order[index]:
				return False
			else:
				continue
		return False
	
	def is_identity(self):
		identity = True
		for index in range(self.size - 1):
			if self.order[index] > self.order[index + 1]:
				identity = False
				break
		return identity
	
	def next(self): 
		# Update the Array Code to the next's permutation code.
		quotient = 1
		index = self.size - 2
		while quotient != 0 and index != -1:
			new_value_at_index = self.array_code[index] + 1
			module = self.size - index
			quotient = new_value_at_index // (module)
			self.array_code[index] = new_value_at_index % module
			index -= 1
		
		# Update the element order.

		## Creating the list of elements to introduce
		resting_elements = []
		for index in range(self.size):
			resting_elements.append(index)

		## Adding them in order.	
		for index in range(self.size - 1): # The last element will be done manually.
			self.order[index] = resting_elements.pop(self.array_code[index])
		self.order[self.size - 1] = resting_elements[0] # Adding the last one

class PermutationGeneratorRecursive():
	def __init__(self, number_of_elements):
		self.permutation_list = []
		self.number_of_elements = number_of_elements
		self.actual_permutation = []

	def __str__(self):
		print_list = []
		for permutation in self.permutation_list:
			print_list.append(str(permutation))
		return str(print_list)

	def start(self):
		if len(self.actual_permutation) == self.number_of_elements:
			self.permutation_list.append(Permutation(self.actual_permutation))
		else:
			for candidate_to_join_permutation in range(self.number_of_elements):
				if candidate_to_join_permutation in self.actual_permutation:
					continue
				else:
					# Añadir el elemento.
					self.actual_permutation.append(candidate_to_join_permutation) 
					# Procesar con el elemento añadido.
					self.start()
					# Una vez procesado, retirarlo y pasar al siguiente ciclo del bucle.
					self.actual_permutation.pop()

class PermutationGeneratorIterative():
	def __init__(self, number_of_elements):
		self.permutation_list = []
		self.number_of_elements = number_of_elements
		self.actual_permutation = Permutation(range(self.number_of_elements))

	def __str__(self):
		print_list = []
		for permutation in self.permutation_list:
			print_list.append(str(permutation))
		return str(print_list)

	def add_permutation(self, permutation):
		self.permutation_list.append(Permutation(self.actual_permutation.order))

	def start(self): # Execution using «next».
		is_iden = False

		while not is_iden:
			self.add_permutation(self.actual_permutation)
			self.actual_permutation.next()
			is_iden = self.actual_permutation.is_identity()

n = 4
recursive = PermutationGeneratorRecursive(n)
iterative = PermutationGeneratorIterative(n)
recursive.start()
iterative.start()
print(recursive)
print(iterative)
