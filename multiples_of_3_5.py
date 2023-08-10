multiples_sum = 0

for i in range(1000):
    #print(i%3)
    #print(i%5)
    if i % 3 == 0 or i % 5 == 0:
        multiples_sum = multiples_sum + i
    
print(multiples_sum)

