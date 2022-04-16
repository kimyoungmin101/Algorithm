# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]

s = [list(map(int, input().split())) for i in range(n)]

    
for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1] - dp[i][j]) + s[i][j]

ans = []        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split()) # 2 2 3 4
    answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    
    ans.append(answer)

for i in ans:
    print(i)