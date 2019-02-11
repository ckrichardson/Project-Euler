fibo_one = 1
fibo_two = 2
fibo_three = 3

sum = 2

while fibo_three < 4000000:
    fibo_one = fibo_two
    fibo_two = fibo_three
    fibo_three = fibo_one + fibo_two

    if not fibo_three % 2:
        sum += fibo_three

print("The sum of all even fibonacci numbers to 4000000 is " + str(sum))
