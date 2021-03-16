def find_two_values (array, target):
    array.sort()
    index_1 = 0
    index_2 = len(array) - 1
    while index_1 != index_2:
        if array[index_1] + array[index_2] == target:
            return (array[index_1], array[index_2])
        elif array[index_1] + array[index_2] < target:
            index_1 += 1
        else:
            index_2 -= 1
    return (0,0) # If there is no solution.

def test():
    array = [1,4,5,6,7,9,9,10]
    target = 12
    print(find_two_values(array, target))
test()