from random import randint 

def generate_random_list(length_of_the_list, max_element_in_the_list):
    random_list = []
    i = 0
    while i < length_of_the_list:
        random_list.append(randint(0,max_element_in_the_list)) 
        i += 1  
    return random_list

def generate_random_list_without_element(length_of_the_list, max_element_in_the_list):
    random_list = []
    element_not_in = randint(0, max_element_in_the_list)
    i = 0   
    while i < length_of_the_list:
        new_element = randint(0, max_element_in_the_list)
        if element_not_in != new_element: 
            random_list.append(new_element) 
            i += 1  
    return (random_list, element_not_in)