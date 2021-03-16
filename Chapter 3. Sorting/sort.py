def merge_two_lists_ordered (list_1, list_2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1
    
    if i == len(list_1):
        while j < len(list_2):
            merged_list.append(list_2[j])
            j += 1
    else:
        while i < len(list_1):
            merged_list.append(list_1[i])
            i += 1
    
    return merged_list

    

def sort (list_to_sort):
    lenght = len(list_to_sort)
    if lenght == 1:
        return list_to_sort
    else:
        return merge_two_lists_ordered(sort(list_to_sort[:lenght//2]), sort(list_to_sort[lenght//2:]))


