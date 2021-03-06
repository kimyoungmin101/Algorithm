from sys import stdin
from math import inf

n = 3
m = 2

# 이동 최소비용을 저장할 2차원 배열
cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for i in cost:
    print(i)

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
print(" ")
for i in cost:
    print(i)

# input
'''
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''

#output
'''
[0, 2, 3, 1, 4]
[12, 0, 15, 2, 5]
[8, 5, 0, 1, 1]
[10, 7, 13, 0, 3]
[7, 4, 10, 6, 0]
'''
