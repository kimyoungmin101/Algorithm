N, M = map(int, input().split())

A = min(N, M)

max = 0
for i in range(1, A+1):
    if(N % i == 0 and M % i == 0 and i > max):
        max = i

print(max)

A = N
B = M

while(True):
    if(N == M):
        print(N)
        break
    else:
        if(N > M):
            M += B
        elif(M > N):
            N += A

