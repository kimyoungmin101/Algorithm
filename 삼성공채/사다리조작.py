# https://www.acmicpc.net/problem/15684
import sys

N, M, H = map(int, sys.stdin.readline().split())

'''
1. 3번 이상이면 그냥 -1 출력하셈
2. visit 같은거 쓰지마셈
3. 중복 안되게 하셈
4. 자기 위치 갈 수 있는지 확인할 때 하나라도 안되면 바로 안되는 걸로 하셈
'''

board = [[0 for _ in range(N)] for _ in range(H)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1
    board[A][B] = 1

    
def check(arr):
    for i in range(len(arr[0])-1):
        start = i
        for j in range(len(arr)):
            if arr[j][start] == 1:
                start += 1
                continue
            elif start - 1 >= 0 and arr[j][start-1] == 1:
                start -= 1
                continue
        if start != i:
            return False
    return True


global ans

ans = 4

def dfs(cnt, start_X, start_Y):
    global ans
    
    if check(board):
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(start_X, len(board)):
        if start_X != i:
            start_Y = 0
        for j in range(start_Y, len(board[0]) - 1):
            if board[i][j] == 0:
                if 0 < j and board[i][j-1] == 1:
                    continue
                if j < N-1 and board[i][j+1] == 1:
                    continue
                
                board[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                board[i][j] = 0
                
            
dfs(0, 0, 0)

if ans > 3:
    print(-1)
else:
    print(ans)
    
    