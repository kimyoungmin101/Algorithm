def pabo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return pabo(n-1) + pabo(n-2)

Q = int(input())

print(pabo(Q))
