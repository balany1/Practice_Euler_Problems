an_int = 13579

def isPalindrome(S):
   S = str(S)
   count = 0
   for i in range (len(S)):
      n = len(S)
      if S[i] == S[n-i-1]:
         count = count+1
         if count == len(S):
            S = int(S.join(S))
            return True
         
def check_factors(S):
    a = 0
    for i in range(100,999):
        if S / i < 1000 and S % i == 0:
            return S
    return a
    
   
            
      
for S in reversed(range(10000,1000000)):
    if isPalindrome(S) == True and check_factors(S) > 0:
          print(S)
          break

             






