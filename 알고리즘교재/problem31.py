# 금광
T = int(input())
dx = [-1,1,0] # 오른쪽위 오른쪽아래 오른쪽
dy = [1,1,1] # 
result = []
for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    board = []
    
    for i in range(0, len(arr), M):
        board.append(arr[i:i+M])
        
    ans = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        ans[i][0] = board[i][0]
    max_result = 0
    for i in range(M):
        for j in range(N):
            for k in range(3):
                X = j + dx[k]
                Y = i + dy[k]
                if X < 0 or Y < 0 or X >= N or Y >= M:
                    continue
                ans[X][Y] = max(ans[X][Y], ans[j][i] + board[X][Y])
                max_result = max(ans[X][Y], max_result)
    
    result.append(max_result)

for i in result:
    print(i)
'''
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
'''