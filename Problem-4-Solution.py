def make_palindrome(number):
    return int(str(number) + str(number)[::-1])

def find_factors(palindrome, max_factor, min_factor, digits, loops):

    counter = max_factor

    while counter >= max_factor - int(min_factor/2):
        if palindrome % counter == 0:
            factor_one = counter
            factor_two = int(palindrome / counter)
            # print(str(palindrome))
            # print(factor_two)

            if len(str(factor_two)) != digits:
                None
            else:
                return factor_one, factor_two, loops

        counter -= 1
        loops += 1

    return 0, 0, loops

################################################################################

print("Enter the amount of digits that the program should consider")
digits = int(input())

max_factor, min_factor = (10 ** digits) - 1, (10 ** (digits - 1))

maximum, minimum = max_factor ** 2, min_factor ** 2

temp, factor_one, factor_two = 0, 0, 0

palindrome = maximum
loops = 0
half_of_digits = int(palindrome / (10 ** digits))
palindrome = make_palindrome(half_of_digits)

while factor_one == 0:
    factor_one, factor_two, loops = find_factors(palindrome, max_factor, min_factor, digits, loops)
    half_of_digits = int((palindrome / (10 ** digits)) - 1)

    if half_of_digits < 0:
        print("No values found!")
        exit()

    palindrome = make_palindrome(half_of_digits)
    loops += 1

print("{0} and {1}".format(str(factor_one), str(factor_two)) + " found in {0} loops".format(str(loops)))


