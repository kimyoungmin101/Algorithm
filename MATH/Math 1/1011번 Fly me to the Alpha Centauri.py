from math import sqrt
T = int(input())

for i in range(T):
    x, y = map(int, input().split())

    q = y - x

    y = int(sqrt(q))
    z = y + 1
    
    if(q == 1):
        print(q)
    elif(q >= y*z+1):
        print(y+z)
    elif(q >= y**2 + 1):
        print(y*2)
    else:
        print(y*2-1)
