# ㅂㅐㅁ


# 벽이나 몸에 부딪히면 끝남,
from collections import deque

N = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input()) # 사과의 개수

for i in range(K):
    A, B = map(int, input().split())
    board[A-1][B-1] = 1

L = int(input()) # 뱀의 방향 변환 횟수

change = []

for i in range(L):
    A, B = map(str, input().split())
    A = int(A)
    
    change.append([A, B])

direct = [[0,1],[1,0],[0,-1],[-1,0]] # 오 아 왼 위
cnt_direct = 0 # 오른쪽

change.sort()

stack = deque([[0,0]])
second = 0
    
while True:
    cnt_X = stack[0][0]
    cnt_Y = stack[0][1]
    
    go_X = direct[cnt_direct][0]
    go_Y = direct[cnt_direct][1]
    
    new_X = cnt_X + go_X
    new_Y = cnt_Y + go_Y
    
    if new_X < 0 or new_Y < 0 or new_X >= N or new_Y >= N: # 벽을 넘는다면
        break
    
    if board[new_X][new_Y] == 1: # 사과가 있다면
        if [new_X, new_Y] in stack: # 자신의 몸과 부딪힌 다면
            break
        stack.appendleft([new_X, new_Y])
        board[new_X][new_Y] = 0
    else: # 사과가 없다면
        if [new_X, new_Y] in stack: # 자신의 몸과 부딪힌 다면
            break
        A, B = stack.pop()
        stack.appendleft([new_X, new_Y])
    
    second += 1
    
    if len(change) >= 1:
        if second == change[0][0]: # 방향 전환
            if change[0][1] == 'D':
                cnt_direct += 1
                if cnt_direct > 3:
                    cnt_direct = 0
            else:
                cnt_direct -= 1
                if cnt_direct < 0:
                    cnt_direct = 3
            change.pop(0)
    
print(second + 1)