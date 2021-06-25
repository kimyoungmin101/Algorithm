def facto(n):
    if(n == 0):
        return 1
    elif(n == 1):
        return 1
    else:
        return n * facto(n-1)

N = int(input())

print(facto(N))
