from generate_random_list import generate_random_list
from generate_random_list import generate_random_list_without_element
from binary_search import binary_search_recursive
from binary_search import binary_search_iterative

def test_with_element_in(search_function):
    number_of_random_tests = 1
    success = True
    while number_of_random_tests > 0:

        random_list = generate_random_list(100, 100)
        element_to_search = random_list[0]
        random_list.sort()

        if not random_list.index(element_to_search) == search_function(random_list, element_to_search):
            success = False
            break
        number_of_random_tests -= 1
    return success

def test_with_element_not_in(search_function):
    number_of_random_tests = 10
    success = True
    while number_of_random_tests > 0:
        random_list, element_to_search = generate_random_list_without_element(100, 100)
        random_list.sort()
        if search_function(random_list, element_to_search) != -1:
            success = False
            print((random_list, element_to_search))
            break
        number_of_random_tests -= 1
    return success

if test_with_element_in(binary_search_recursive) and test_with_element_not_in(binary_search_recursive):
    print('binary_search_recursive: Pass!')
else:
    print('binary_search_recursive: Fail!')

if test_with_element_in(binary_search_iterative) and test_with_element_not_in(binary_search_iterative):
    print('binary_search_iterative: Pass!')
else:
    print('binary_search_iterative: Fail!')