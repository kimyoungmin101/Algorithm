# 금광
'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''
T = int(input())

for cnt in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    board = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N * M):
        value_X = i // M
        value_Y = i % M
        
        board[value_X][value_Y] = arr[i]
        
    
    for Y in range(1, M):
        for X in range(N):
            # 왼쪽 위
            left_up = 0
            # 왼쪽
            left = 0
            # 왼쪽 아래
            left_down = 0
            
            cnt_value = board[X][Y]
            
            if X - 1 >= 0:
                left_up = board[X-1][Y-1] + cnt_value
            left = board[X][Y-1] + cnt_value
            if X + 1 < N:
                left_down = board[X+1][Y-1] + cnt_value
            
            board[X][Y] = max(left_up, left, left_down)
    
    board = list(zip(*board[::-1]))
               
    max_size = 0
    for i in board:
        max_len = max(i)
        max_size = max(max_size, max_len)
    
    print(max_size)
            
            
'''
1 3 1 5
2 2 4 1
5 0 2 3
0 6 1 2
'''