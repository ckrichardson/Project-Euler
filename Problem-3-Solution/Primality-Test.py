def prime_number_sieve(number):
    prime_list = [1] * number;

    for x in range(number):
        for y in range(x, number):
            if not number % y:
                prime_list[y] = 0;

    return prime_list