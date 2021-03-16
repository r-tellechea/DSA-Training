def construct_sorted_list(bookkeeping):
    construct = []
    for element in range(len(bookkeeping)):
        construct += [element]*bookkeeping[element]
    return construct

def counting_sort(list_to_sort, max_element_in_the_list):

    bookkeeping = [0] * (max_element_in_the_list + 1) # From 0 to n there are n+1 possible elements.
    for element_in_the_list in list_to_sort:
        bookkeeping[element_in_the_list] += 1
    return construct_sorted_list(bookkeeping)

