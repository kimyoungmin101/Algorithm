# 치킨배달
import sys
from itertools import combinations

result = []

def dfs(arr, size, cnt_arr):
    if len(cnt_arr) == size:
        cnt_arr.sort()
        if cnt_arr not in result:
            result.append(cnt_arr.copy())
        return
    
    start = arr.index(cnt_arr[-1]) + 1 if cnt_arr else 0
    for i in range(start, len(arr)):
        if arr[i] not in cnt_arr:
            cnt_arr.append(arr[i])
            dfs(arr, size, cnt_arr)
            cnt_arr.pop()

N, M = map(int, input().split())
# 0은 빈 칸, 1은 집, 2는 치킨
board = []

min_cnt = sys.maxsize

for i in range(N):
    board.append(list(map(int, input().split())))     

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            board[i][j] = 0
            chicken.append([i,j])
        if board[i][j] == 1:
            house.append([i,j])

dfs(chicken, M, [])

def len_which(A, B):
    # |r1-r2| + |c1-c2|
    X = abs(A[0] - B[0])
    Y = abs(A[1] - B[1])
    return X + Y

result_ans = sys.maxsize

for i in result:
    answer = 0
    for home in house:
        min_result = sys.maxsize # 가장 작은 거리
        for chick in i:
            min_result = min(len_which(chick, home), min_result)
        answer += min_result
    
    result_ans = min(result_ans, answer)

print(result_ans)

