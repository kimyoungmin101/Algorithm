N = int(input())
board = []

for i in range(N):
    board.append(list(map(int, input().split())))

cnt = 2
for i in range(1, N):
    for j in range(cnt):
        if j == 0:
            board[i][j] += board[i-1][j]
        elif j == cnt - 1:
            board[i][j] += board[i-1][j-1]
        else:
            left_value = board[i][j] + board[i-1][j-1]
            right_value = board[i][j] + board[i-1][j]
            board[i][j] = max(left_value, right_value)
    cnt += 1

print(max(board[-1]))