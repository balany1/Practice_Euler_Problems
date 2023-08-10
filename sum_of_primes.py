from math import sqrt

# Number to be checked for prime

prime_list = []
prime_sum = 0

def is_prime(n): # same as before
    for D in range(2, n):
        if (D * D > n):          # first added line
            break                  # second added line
        if n % D == 0:
            return
    prime_list.append(n)
    
def sum_n_primes(n):
	
	i = 2
	while True:
             if i>n:
                  print(prime_list)
                  break
             else:
                  is_prime(i)
                  i = i+1
    
n = int(input())	
sum_n_primes(n)

for prime in prime_list:
     prime_sum = prime_sum + prime
print(prime_sum)
     