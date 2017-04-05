def find_max_min(list_value):
    """
    
    Function that returns the maximum and minimum values in a list_value

    """
    if len(set(list_value)) > 1:
        return [min(list_value), max(list_value)]
    else:
        return [list_value[0]]


print(find_max_min([1, 2, 3, 4]))
print(find_max_min([6, 4]))
print(find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]))
print(find_max_min([1, 2, 3, 4]))
print(find_max_min([4, 4, 4, 4]))
