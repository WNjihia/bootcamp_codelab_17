def fizz_buzz(num):
    """
    function to return 'Fizz', 'Buzz', 'FizzBuzz' or the argument
    depending on the argument of the function being divisible by
    3, 5 or both 3 and 5 repectively

    """
    if (num % 3 == 0) and (num % 5 != 0):
        return 'Fizz'
    elif (num % 3 != 0) and (num % 5 == 0):
        return 'Buzz'
    elif (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    else:
        return num


print(fizz_buzz(9))
print(fizz_buzz(15))
print(fizz_buzz(25))
