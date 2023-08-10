from math import sqrt

# Number to be checked for prime

prime_list = []

def is_prime(n):
    
    flag = 0

    if(n > 1):
        for i in range(2,n):
            if (n%i) == 0:
                return False
        prime_list.append(n)
        return True
	

def first_n_primes(n):
	
	i = 0
	while True:
             if len(prime_list) == n:
                  print(prime_list[-1])
                  break
             else:
                  is_prime(i)
                  i = i+1


n = int(input())	
first_n_primes(n)	
