# 화성탐사
'''

3  
3  
5 5 4  
3 9 1  
3 2 7  
5  
3 7 2 0 1  
2 8 0 9 1  
1 2 1 8 1  
9 8 9 2 0  
3 6 5 1 5  
7  
9 0 5 1 1 5 3  
4 1 2 1 6 5 3  
0 7 6 1 6 8 5  
1 1 7 8 3 2 3  
9 4 0 7 6 4 1  
5 8 3 2 4 8 3  
7 4 8 4 8 3 4

'''
import heapq
import sys

T = int(input())

for cnt in range(T):
    N = int(input())
    board = []
    weights = [[sys.maxsize-1 for _ in range(N)] for _ in range(N)]
    heap = []
    
    for X in range(N):
        board.append(list(map(int, input().split())))
    
    weights[0][0] = board[0][0]
    
    heapq.heappush(heap, [weights[0][0], 0, 0])
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while heap:
        weight, X, Y = heapq.heappop(heap) # 5 0 0
        for i in range(4):
            real_X = dx[i] + X
            real_Y = dy[i] + Y
            
            if real_X < 0 or real_Y < 0 or real_X >= N or real_Y >= N:
                continue
                
            if board[real_X][real_Y] + weights[X][Y] < weights[real_X][real_Y]:
                weights[real_X][real_Y] = board[real_X][real_Y] + weights[X][Y]
                heapq.heappush(heap, [weights[real_X][real_Y], real_X, real_Y])
                
    
    print(weights[-1][-1])