# 백준 부분수열의합 1182번 문제 / https://www.acmicpc.net/problem/1182

import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    combi = list(combinations(arr, i+1))
    for k in combi:
        if sum(k) == s:
            cnt += 1

print(cnt)
