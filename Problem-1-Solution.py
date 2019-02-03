multiples_of_three = set()
multiples_of_five = set()

print("Enter the number for up until we want to find all multiples of three and five")
user_input = int(input())

for x in range(user_input):
    if not x % 3:
        multiples_of_three.add(x)
    if not x % 5:
        multiples_of_five.add(x)

whole_set = multiples_of_three | multiples_of_five
sum = 0

for element in whole_set:
    sum += element

print("\nSum of all multiples of three and five between 1 and " + str(user_input) + ":   " + str(sum))