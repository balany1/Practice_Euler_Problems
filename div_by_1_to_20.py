import numpy

def get_prime_factors(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
    
    return prime_factors

def additional_prime_factors(n):
    a = n
    for i in prime_factors:
        if n % i == 0:
            a = a / i
    return a

for i in range(2,20):
    prime_factors = prime_factors.append(get_prime_factors(i))
    print(prime_factors)
    a = additional_prime_factors(i)
    print(a)
    #prime_factors.append(a)


#print(numpy.prod(prime_factors))