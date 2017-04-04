def gen_prime_number(value):
    prime_numbers_list = []
    for element in range(2, value+1):
        isPrime = True
        for num in range(2, element):
            if element % num == 0:
                isPrime = False
        if isPrime:
            prime_numbers_list.append(element)
    return prime_numbers_list


print(gen_prime_number(10))
