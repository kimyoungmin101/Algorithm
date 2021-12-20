N = int(input())

for i in range(N):
    A, B = map(int, input().split())
    C = A
    D = B
    while(C != D):
        if(C < D):
            C += A
            continue
        else:
            D += B
            continue
    print(C)
