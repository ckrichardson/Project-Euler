multiples_of_three = set()
multiples_of_five = set()

print("Enter the number for up until we want to find all multiples of three and five")
user_input = int(input())

x = 0
counter = 0

for x in range(0, user_input, 3):

    multiples_of_three.add(x)
    if x + (2 * counter) < user_input:
        multiples_of_five.add(x + int((2 * counter)))
        counter += 1


whole_set = multiples_of_three | multiples_of_five
sum = 0

for element in whole_set:
    sum += element

print("\nSum of all multiples of three and five between 1 and " + str(user_input) + ":   " + str(sum))