print("Enter the number for up until we want to find all multiples of three and five")
user_input = int(input())

counter = 0
sum = 0

for x in range(3, user_input, 3):
    if x % 5:
        sum += x
    counter += 1
    if x + int(2 * counter) < user_input:
        print(str(x + int(2 * counter)))
        sum += x + int(2 * counter)


print("\nSum of all multiples of three and five between 1 and " + str(user_input) + " is " + str(sum) + ", calculated "\
        + "in " + str(counter) + " loops!")