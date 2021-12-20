N, M = map(int, input().split())

Q = list(map(int,input().split()))

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            A = Q[i] + Q[j] + Q[k]
            if( ans < A ):
                if( A <= M):
                    ans = A

print(ans)
            
