# 못생긴 수

N = int(input())

DP = [0 for _ in range(1001)]
DP[0] = 0
DP[1] = 1

for i in range(2, 1001):
    ans = i
    if ans % 2 == 0:
        ans //= 2
    if ans % 3 == 0:
        ans //= 3
    if ans % 5 == 0:
        ans //= 5
    
    if DP[ans] != 0:
        DP[i] = i
    else:
        DP[i] = 0

result = [DP[i] for i in range(1001) if DP[i] != 0]
print(result[N-1])

# 2 3 5 만 약수
# 0 1 2 3 4 5 6 8 9 10 12

