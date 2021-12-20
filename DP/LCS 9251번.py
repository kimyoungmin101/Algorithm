A = input()
B = input()

arrA = []
arrB = []

for i in A:
    arrA.append(i)

for i in B:
    arrB.append(i)

DP = [[0] * (len(arrB)+1) for _ in range(len(arrA)+1)]

for i in range(1, len(arrA)+1):
    for j in range(1, len(arrB)+1):
        if(arrA[i-1] == arrB[j-1]):
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

print(DP[-1][-1])
