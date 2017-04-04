def gen_prime_number(value):
    """
    function to generate a list of prime numbers within a certain range

    args: value which is the upper limit for the range

    returns a list of prime numbers
    """
    if isinstance(value, int):
        if value > 1:
            prime_numbers_list = []
            for element in range(2, value+1):
                isPrime = True
                for num in range(2, element):
                    if element % num == 0:
                        isPrime = False
                if isPrime:
                    prime_numbers_list.append(element)
        else:
            return 'Invalid input'
    else:
        raise ValueError
    return prime_numbers_list


print(gen_prime_number(10))
