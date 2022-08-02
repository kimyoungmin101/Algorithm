# 무지의 먹먹방방라라이이브

import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return - 1
    heap = []
    
    for idx, value in enumerate(food_times):
        heapq.heappush(heap, [value, idx+1])
    
    value = 0
    
    while (len(heap) * (heap[0][0] - value)) <= k:            
        A = heap[0]
        
        if value == A[0]:
            heapq.heappop(heap)
            continue
            
        k -= (len(heap) * (A[0] - value))
        value = A[0]
        heapq.heappop(heap)
    
    result = sorted(heap, key = lambda X : X[1])
    
    
    if len(result) == 0:
        return - 1
    else:
        return result[k % len(result)][1]
    
