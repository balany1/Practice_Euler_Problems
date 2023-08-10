
comp_num = 600851475143
for i in range(2,600851475143):
    if comp_num % i == 0:
        if comp_num == i:
            print(i)
            break
        comp_num = comp_num/i
        i = 2

