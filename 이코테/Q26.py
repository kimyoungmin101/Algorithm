import heapq

N = int(input())

arr = []

sum_cnt = 0

for i in range(N):
    heapq.heappush(arr, int(input()))

while arr:
    A = heapq.heappop(arr)
    if len(arr) == 0:
        break
    B = heapq.heappop(arr)
    
    C = A + B
    sum_cnt += C
    
    heapq.heappush(arr, C)
    
print(sum_cnt)