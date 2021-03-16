class Sequence ():
    def __init__(self, sequence):
        self.sequence = sequence

    def longest_sequence_size_n2 (self):
        length_array = [1] * len(self.sequence)
        for index, element in enumerate(self.sequence):
            for sub_index, sub_element in enumerate(self.sequence[:index]):
                if sub_element < element:
                    length_array[index] = max(length_array[index], 1 + length_array[sub_index])
            print(length_array[index])
        return max(length_array)
    
    def longest_sequence_size_n (self):
        return 0 # To do

s = Sequence([6,2,5,1,7,4,8,3])
print(s.longest_sequence_size_n2())