# https://www.acmicpc.net/problem/14712

 
N, M = map(int, input().split())

board = [[0] * (M+1) for _ in range(N+1)]
cnt = 0

def recursive(X,Y):
    global cnt, N, M
    
    if Y > M:
        X += 1
        Y = 1
    
    if X > N:
        return
    
    
    # 네모를 놓을 때
    if board[X-1][Y] == 0 or board[X][Y-1] == 0 or board[X-1][Y-1] == 0:
        cnt += 1
        board[X][Y] = 1
        recursive(X, Y+1)
        board[X][Y] = 0
        
    # 네모를 놓지 않을 때
    recursive(X, Y+1)
    
    return

recursive(1,1)

print(cnt+1)