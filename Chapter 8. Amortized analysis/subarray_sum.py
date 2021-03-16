def subarray_sum (array, target):
    """
    · array : List[int], all possitive numbers.
    · target : int, > 0.
    """
    index_1 = 0
    index_2 = 0
    while index_1 < len(array) and index_2 < len(array):
        if sum(array[index_1: index_2 + 1]) == target:
            return (index_1, index_2)
        elif sum(array[index_1: index_2 + 1]) < target:
            while sum(array[index_1: index_2 + 1]) < target:
                index_2 += 1
        else:
            index_1 += 1
    return (0,0) # No subarray found

def test():
    array = [1,3,2,5,1,1,2,3]
    target = 8
    print(subarray_sum(array, target))