fib_1 = 1
fib_2 = 1
fib_sum = 0

while fib_sum <=4000000:
    fib_3 = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_3
    if fib_3 % 2 == 0:
        fib_sum = fib_sum + fib_3

print(fib_sum)
    