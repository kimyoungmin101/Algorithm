import heapq

N, M, K, X = list(map(int, input().split()))

dic = {}

for i in range(M):
    A, B = map(int, input().split())
    if A not in dic:
        dic[A] = [B]
    else:
        dic[A].append(B)


def dkstra(dic):
    heap = []

    weight = [1000001 for _ in range(N + 1)]
    weight[0] = 0
    weight[X] = 0

    for i in dic[X]:
        if weight[i] > weight[X] + 1:
            weight[i] = weight[X] + 1
            heapq.heappush(heap, i)
    
    
    
    while heap:
        A = heapq.heappop(heap) # [2], [3]
        if A in dic:
            for i in dic[A]:
                if weight[i] > weight[A] + 1:
                    weight[i] = weight[A] + 1
                    heapq.heappush(heap, i)
                
    return weight

answer = dkstra(dic)
result = []
for idx, value in enumerate(answer):
    if value == K:
        result.append(idx)
    
if len(result) == 0:
    print(-1)
else:    
    for i in result:
        print(i)
    