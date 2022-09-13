# https://www.acmicpc.net/problem/17822
from collections import deque
from copy import deepcopy

N, M, T = map(int, input().split())

board = []

for i in range(N):
    board.append(deque(list(map(int, input().split()))))

ans = []

def bfs(new_board, N_X, N_Y):
    global N, M
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    new_visit = [[N_X, N_Y]]
    q = deque([[N_X, N_Y]])
    
    while q:
        cnt_X, cnt_Y = q.popleft()
        rotate_N = 4
        
        for i in range(rotate_N):
            new_X = cnt_X + dx[i]
            new_Y = cnt_Y + dy[i]
            
            if new_X < 0 or new_Y < 0 or new_X >= N or new_Y >= M:
                if new_Y == -1:
                    new_Y = M-1
                elif new_Y == M:
                    new_Y = 0
                else:
                    continue
            
            if new_board[cnt_X][cnt_Y] == new_board[new_X][new_Y] and [new_X, new_Y] not in new_visit:
                q.append([new_X, new_Y])
                new_visit.append([new_X, new_Y])

    return new_visit

for i in range(T):
    new_copy = deepcopy(board)
    
    X, D, K = map(int, input().split())
    
    circle = [] # 몇배수의 원판들을 사용할것인지
    
    for j in range(X, N+1, X):
        circle.append(j)
    
    for j in circle:
        if D == 0: # 시계방향
            new_copy[j-1].rotate(K)
        else:
            new_copy[j-1].rotate(-K)
    
    # 인접한수 지우기
    
    rotate_cnt = 0
    visit = []
    for x in range(N):
        for y in range(M):
            if new_copy[x][y] != 0:
                cnt_visit = bfs(new_copy, x , y)
                
                if len(cnt_visit) >= 2:
                    rotate_cnt += 1
                    for k in cnt_visit:
                        new_copy[k[0]][k[1]] = 0
    
    if rotate_cnt == 0:
        # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
        cnt = 0
        sum_result = 0
        for x in range(N):
            for y in range(M):
                if new_copy[x][y] != 0:
                    cnt += 1
                    sum_result += new_copy[x][y]
                    
        if cnt != 0 and sum_result != 0:
            avar = float(sum_result / cnt)
        
            for x in range(N):
                for y in range(M):
                    if new_copy[x][y] != 0:
                        if float(new_copy[x][y]) > avar:
                            new_copy[x][y] -= 1
                        elif float(new_copy[x][y]) < avar:
                            new_copy[x][y] += 1
    
    board = new_copy

result = 0
for x in range(N):
    for y in range(M):
        result += board[x][y]
    
print(result)
        
# X의 배수 원판을
'''
4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 2
'''