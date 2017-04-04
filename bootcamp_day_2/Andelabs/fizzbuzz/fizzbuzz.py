def fizz_buzz(num):
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
