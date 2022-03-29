# 숨바꼭질


'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''

import heapq
import sys

N, M = map(int, input().split())

dic = {}

for i in range(M):
    A, B = map(int, input().split())
    if A not in dic:
        dic[A] = [[A, B]]
    else:
        dic[A].append([A,B])
    
    if B not in dic:
        dic[B] = [[B,A]]
    else:
        dic[B].append([B,A])
    
heap = []
weights = [sys.maxsize for _ in range(N+1)]
weights[0] = 0
weights[1] = 0


for X in dic[1]:
    heapq.heappush(heap, X)
    
while heap:
    prev, cnt = heapq.heappop(heap) # 1, 3
    
    if weights[cnt] > weights[prev] + 1:
        weights[cnt] = weights[prev] + 1
        
        for X in dic[cnt]:
            heapq.heappush(heap, X)

answer_B = max(weights)

answer_A = 0

for idx in range(len(weights)):
    if weights[idx] == answer_B:
        answer_A = idx
        break
    
answer_C = weights.count(answer_B)

print("{} {} {}".format(answer_A, answer_B, answer_C))