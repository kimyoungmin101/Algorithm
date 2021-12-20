T = int(input())

arr = []
for i in range(T):
    arr.append(int(input()))

dp = [0 for _ in range(47)]
dp[0] = 1
dp[1] = 3
dp[2] = 6
# 1 3 6 10 15 21
for i in range(3, 47):
    dp[i] = (dp[i-1] - dp[i-2] + 1) + dp[i-1]


results = 0
for q in arr:
    real_arr = []
    for k in range(len(dp)):
        if q < dp[k]:
            real_arr = dp[:k].copy()
            break
    print(real_arr)

    for i in range(len(real_arr)):
        for j in range(len(real_arr)):
            for k in range(len(real_arr)):
                sum_result = real_arr[i] + real_arr[j] + real_arr[k]
                if(sum_result == q):
                    results = 1
                    break
                
    results = 0