# 1로만들기

X = int(input())

dp = [[X]]
cnt = 0

while True:
    ans = []
    
    for i in dp[cnt]:
        ans.append(i - 1)
        if i % 5 == 0:
            ans.append(i // 5)
        if i % 3 == 0:
            ans.append(i // 3)
        if i % 2 == 0:
            ans.append(i // 2)
        
    dp.append(ans)
    cnt += 1
    print(dp)
    if 1 in dp[-1]:
        print(cnt)
        break
    