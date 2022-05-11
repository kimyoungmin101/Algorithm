# https://www.acmicpc.net/problem/1548

import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

A = list(map(int, input().rstrip().split()))

A.sort()

answer = n

if n>2:
    answer = -1
    for start in range(n-2):
        for end in range(n-1,start+1,-1):
            if A[start]+A[start+1] > A[end]:
                answer = max(answer,end-start+1)

    if answer == -1:
        answer = 2
print(answer)

