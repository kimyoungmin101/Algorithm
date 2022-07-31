# https://www.acmicpc.net/problem/20438

import sys
input = sys.stdin.readline

n,k,q,m = map(int, input().split())
real_sleep = list(map(int, input().split()))

sleep = [0]*(n+3)
check = [0]*(n+3)

arr = list(map(int, input().split()))

for i in arr:
    if i in real_sleep:
        continue
    for j in range(i, n+3, i):
        if j in real_sleep:
            continue
        check[j] = 1


for i in range(1, len(check)):
    check[i] = check[i] + check[i-1]
    
for i in range(m):
    s, e = map(int, input().split())
    print( e - s + 1 - (check[e] - check[s-1]))