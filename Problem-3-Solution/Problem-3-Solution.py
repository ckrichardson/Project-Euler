from math import *

def prime_number_sieve(startNum, number):
    prime_list = [1] * number + [1]

    for x in range(startNum, int(number/2)+1):
        if prime_list[x]:
            for y in range(0+2*x, number+1, x):
                prime_list[y] = 0

    return prime_list

rewrite = False
user_input = int(input())
largest_prime_factor = 0

prime_list = list()

with open("primes.txt", "r") as inputFile:
    nums = list()
    for line in inputFile:
        nums.append(int(line))
        if not len(nums):
         lastNum = 0
    else:
        lastNum = int(nums[len(nums) - 1])
    if lastNum > int(sqrt(user_input)) + 1 and lastNum > 0:
        prime_list = nums
    else:
        prime_list = prime_number_sieve(2, user_input)
        rewrite = True

if rewrite:
    with open("primes.txt", "w") as outputFile:
        for x in range(len(prime_list)):
            if prime_list[x] and x > 1:
                outputFile.write(str(x) + '\n')

print(prime_list)
counter = int(user_input / 3)
index = 0
print(counter)
while prime_list[index] <= counter:
    print(str(prime_list[index]) + " ")
    if user_input % prime_list[index] == 0:
        largest_prime_factor = prime_list[index]
        print(str(user_input) + " divided by " + str(prime_list[index]))
    index += 1

if largest_prime_factor:
    print(largest_prime_factor)
else:
    print("No prime factors - this number is prime!")

