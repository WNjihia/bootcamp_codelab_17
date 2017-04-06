def find_missing(list_one, list_two):
    """

    Function that returns the difference between two lists

    """
    if (len(list_one) == 0) and (len(list_two) == 0): # checks if the lists are empty
        return 0
    if set(list_one) == set(list_two): # checks if lists contain similar values
        return 0
    else:
        diff = set(list_one).symmetric_difference(set(list_two)) # diff is the difference between the lists
    return list(diff)[0] #retrieve first item in the list

print(find_missing([], []))
print(find_missing([1, 2], [1, 2, 5]))
print(find_missing([4], [4]))
