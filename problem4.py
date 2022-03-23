import heapq
import sys
ans_root = []


def solution(N, transfer, trainA, trainB, s, e):
    answer = 0


    dic = {}

    for i in trainA:
        if i[0] not in dic:
            dic[i[0]] = [[i[2], i[1], 'A']]
        else:
            dic[i[0]].append([i[2], i[1] , 'A'])
        if i[1] not in dic:
            dic[i[1]] = [[i[2], i[0], 'A']]
        else:
            dic[i[1]].append([i[2], i[0] , 'A'])

    for i in trainB:
        if i[0] not in dic:
            dic[i[0]] = [[i[2], i[1], 'B']]
        else:
            dic[i[0]].append([i[2], i[1], 'B'])
        if i[1] not in dic:
            dic[i[1]] = [[i[2], i[0], 'B']]
        else:
            dic[i[1]].append([i[2], i[0], 'B'])

    weight = [sys.maxsize - 1 for _ in range(N + 1)]
    weight[s] = 0
    heap = []

    for i in dic[s]:
        if weight[i[1]] > weight[s] + i[0]:
            weight[i[1]] = weight[s] + i[0]
            heapq.heappush(heap, [weight[i[1]], i[1], i[2]])
    
    while heap:
        road, next_idx, train = heapq.heappop(heap)
        
        # [[1, 2, 'A'], [3, 3, 'A']]
        for i in dic[next_idx]: # [1, 1, 'A']
            if i[2] == train:
                if weight[i[1]] >= road + i[0]:
                    weight[i[1]] = road + i[0]
                    heapq.heappush(heap, [weight[i[1]], i[1], i[2]])
            else:
                if weight[i[1]] >= road + i[0] + transfer[next_idx-1]:
                    weight[i[1]] = road + i[0] + transfer[next_idx-1]
                    heapq.heappush(heap, [weight[i[1]], i[1], i[2]])
    
    answer = weight[e]

    return answer