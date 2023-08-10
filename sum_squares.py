import numpy

def sum_squares(input):
    a = 0
    for i in range(0,int(input)+1):
        b = i ** 2
        a = a + b
    print(a)
    return a


def square_sum(input):
    a = 0
    for i in range(0,int(input)+1):
        a = a + i

    print(a)
    b = a**2
    print(b)
    return b

def diff_squares(input):
    diff = square_sum(input) - sum_squares(input)
    print(diff)

a = input()
diff_squares(a)