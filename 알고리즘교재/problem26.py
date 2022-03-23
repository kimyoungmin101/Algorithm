# https://www.acmicpc.net/problem/1715 ㅋㅏ드정렬하기

import heapq

N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

heap = []
for i in arr:
    heapq.heappush(heap, i)

answer = 0

while heap:
    if len(heap) <= 1:
        break
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    C = A + B
    answer += C
    
    heapq.heappush(heap, C)
    

print(answer)

# 30 + 60 + 90 + 150