from math import sqrt



while(True):
    A = list(map(int, input().split()))
    if(A[0] == 0 and A[1] == 0 and A[2] == 0):
        break
    
    maxN = max(A)

    A.remove(maxN)

    ans = 0
    for i in A:
        ans += int(i ** 2)
    if(ans == (int(maxN ** 2))):
        print('right')
    else:
        print('wrong')
    
