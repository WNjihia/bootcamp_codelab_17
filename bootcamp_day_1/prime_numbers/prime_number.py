def gen_prime_number(value):
    if isinstance(value, int):
        prime_numbers_list = []
        if value > 1:
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
