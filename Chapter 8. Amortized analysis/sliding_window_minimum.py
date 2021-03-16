def sliding_window_minimum (array, window_size):
    index = window_size
    minimum_array = [min(array[:window_size])]
    # Start the queue
    queue = [array[0]]
    for element in array[:window_size]:
        while len(queue) != 0 and element < queue[-1]:
            queue.pop(-1)
        queue.append(element)
    # Run the algorithm
    while index < len(array):
        while len(queue) != 0 and (queue[-1] > array[index]):
            queue.pop(-1)
        queue.append(array[index])
        if not queue[0] in array[index - window_size + 1 : index + 1]:
            queue.pop(0)
        minimum_array.append(queue[0])
        index += 1
    return minimum_array

def test ():
    array = [2,1,4,5,3,4,1,2]
    window_size = 4
    print(sliding_window_minimum(array, window_size))
