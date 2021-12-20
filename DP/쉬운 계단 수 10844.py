N = int(input())

DP = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(1, N+1):
    ndp = []
    for j in range(10):
        if(j == 0):
            ndp.append(DP[i-1][j+1])
        elif(j == 9):
            ndp.append(DP[i-1][j-1])
        else:
            ndp.append(DP[i-1][j-1] + DP[i-1][j+1])
    DP.append(ndp)

print(sum(DP[N-1]) % 1000000000)
