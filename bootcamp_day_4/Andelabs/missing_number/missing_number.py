def find_missing(list_one, list_two):
    """

<<<<<<< HEAD
    Function that returns the difference between two lists
=======
    Function that the difference between two lists
>>>>>>> 22290a27e0b588143869d66e3d5c9ceaac3a38a5

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
