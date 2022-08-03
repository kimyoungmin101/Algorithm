# 특정거리 도시찾기
import heapq
import sys

N,M,K,X = map(int, input().split())

dic = {}

heap = []
weight = [sys.maxsize for _ in range(N + 1)]
weight[0] = 0

for i in range(M):
    A, B = map(int, input().split())
    if A not in dic:
        dic[A] = [B]
    else:
        new_dic = dic[A]
        new_dic.append(B)
        dic[A] = new_dic

weight[X] = 0 # X는 출발지점

for i in dic[X]:
    weight[i] = 1
    heapq.heappush(heap, [1, i])


while heap:
    
    A, B = heapq.heappop(heap)
    
    if B in dic:
        for i in dic[B]:
            if weight[i] > A + 1:
                weight[i] = A + 1
                heapq.heappush(heap, [A+1, i])

result = []

if K not in weight:
    print(-1)
else:
    for idx, value in enumerate(weight):
        if value == K:
            result.append(idx)

    result.sort()

    for i in result:
        print(i)