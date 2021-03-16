def nearest_smaller_element (array):
    stack = []
    nearest_array = []
    for element in array:
        while (len(stack) != 0) and (not stack[-1] < element):
            stack.pop(-1)
        if len(stack) != 0:
            nearest_array.append(stack[-1])
        else:
            nearest_array.append(None)
        stack.append(element)
    return nearest_array

def test():
    print(nearest_smaller_element([1,3,4,2,5,3,4,2]))
    