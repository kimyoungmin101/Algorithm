# https://www.acmicpc.net/problem/4485

import heapq
import sys
def dkstra(arr):
    
    weight = [[sys.maxsize for _ in range(len(arr))] for _ in range(len(arr))]
    
    heap = []

    weight[0][0] = arr[0][0]
    heapq.heappush(heap, [arr[0][0], [0,0]])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while heap:
        A, B = heapq.heappop(heap)
        X, Y = B[0], B[1]
        
        for i in range(4):
            new_X = X + dx[i]
            new_Y = Y + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= len(arr) or new_Y >= len(arr):
                continue
            
            if weight[new_X][new_Y] > arr[new_X][new_Y] + A:
                weight[new_X][new_Y] = arr[new_X][new_Y] + A
                heapq.heappush(heap, [weight[new_X][new_Y], [new_X , new_Y]])
        
    return weight

result = []

while True:
    N = int(input())
    
    if N == 0:
        break
    
    board = []
    
    for i in range(N):
        board.append(list(map(int, input().split())))
    
    new_arr = dkstra(board)
    result.append(new_arr[-1][-1])

for i in range(len(result)):
    print("Problem %d: %d" % (i+1, result[i]))