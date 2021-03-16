# This test only checks if the returned list is ordered, but not if its the ordered version of the original one.

from generate_random_list import generate_random_list
from sort import sort
from counting_sort import counting_sort

def check_sorted_list(sorted_list):
    succesfull = True
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] > sorted_list[i+1]:
            succesfull = False
            break
    return succesfull

def check_list_elements(original_list, sorted_list):
    succesfull = True
    for element in set(original_list):
        if original_list.count(element) != sorted_list.count(element):
            succesfull = False
            break
    return succesfull


# Creating a random list.

length_of_the_list = 10
max_element_in_the_list = 100

random_list = generate_random_list(length_of_the_list, max_element_in_the_list)
# Sorting the list in different ways.

sorted_random_list_1 = sort(random_list)
sorted_random_list_2 = counting_sort(random_list, max_element_in_the_list)

if check_sorted_list(sorted_random_list_1) and check_list_elements(random_list, sorted_random_list_1):
    print("'sort': Pass!")
else: 
    print("'sort': Fail!")

if check_sorted_list(sorted_random_list_2) and check_list_elements(random_list, sorted_random_list_2):
    print("'counting_sort': Pass!")
else: 
    print("'counting_sort': Fail!")

