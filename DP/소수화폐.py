from itertools import product
n = int(input())

a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

DP = [0]*40001
 
DP[0] = 1
for prime_number in primes:
    for num in range(prime_number,n+1):
        DP[num] = (DP[num]+DP[num-prime_number])%123456789
 
print(DP[n])

# 9 -> 2 7 / 2 2 2 3 / 3 3 3 / 2 2 5 
#  0 1 2 3 4 5 6 7 8,9,10
# [0,0,1,1,1,2,2,3,3,4,4,]

# 2 / 2 5 / 7 / 2 3