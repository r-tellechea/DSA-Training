class Subset ():
	def __init__(self, elements):
		self.elements = []
		for element in elements:
			self.elements.append(element)
		self.elements.sort()

	def __str__(self):
		return str(self.elements)

	def __lt__(self, other):
		included = True
		for element in self.elements:
			if not element in other.elements:
				included = False
				break
		return included
	
	def __le__(self, other):
		return self.__lt__(other) or self.elements == other.elements

class SubsetGeneratorRecursive():
	def __init__(self, number_of_elements):
		self.number_of_elements = number_of_elements
		self.subsets = []

	def __str__(self):
		print_list = []
		for subset in self.subsets:
			print_list.append(str(subset))
		return str(print_list)

	def add_subset_found (self, subset):
		self.subsets.append(Subset(subset))
		#self.subsets.sort()

	def search(self, subset, new_element):
		if new_element == self.number_of_elements:
			self.add_subset_found(subset)
		else:
			self.search(subset, new_element + 1)
			subset.append(new_element)
			self.search(subset, new_element + 1)
			subset.pop()

	def start(self):
		original_subset = []
		self.search(original_subset, 0)


def search(subset_list, subset, k):
	if k == 3:
		subset_copy = []
		for element in subset:
			subset_copy.append(element)
		subset_list.append(subset_copy)
	else:
		search(subset_list, subset, k+1)
		subset.append(k)
		search(subset_list, subset, k+1)
		subset.pop()
	

class SubsetGeneratorIterative():
	def __init__(self, number_of_elements):
		self.number_of_elements = number_of_elements
		self.subsets = []

	def __str__(self):
		print_list = []
		for subset in self.subsets:
			print_list.append(str(subset))
		return str(print_list)
	
	def start(self):
		self.subsets.append([])
		k = 0
		while k < self.number_of_elements:
			subset_index = 0
			subset_size = len(self.subsets)
			while subset_index < subset_size:
				self.subsets.append(self.subsets[subset_index] + [k])
				subset_index += 1
			k += 1

		

recursive = SubsetGeneratorRecursive(4)
iterative = SubsetGeneratorIterative(4)
recursive.start()
iterative.start()
print(recursive)
print(iterative)

#sub_list = []
#search(sub_list, [], 0)
#print(sub_list)
