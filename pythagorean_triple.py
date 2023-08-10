triple_list = []

def check_triple(a,b,c):
    #q=0
    if a**2 + b**2 == c**2:
        triple_list.append((a,b,c,a+b+c))
        

for i in range(1,500):
    for j in range(i,500):
        for k in range(j,500):
            check_triple(i,j,k)

for triple in triple_list:
    if triple[3] == 1000:
        print(triple[0]*triple[1]*triple[2])