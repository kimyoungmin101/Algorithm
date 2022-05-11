# https://www.acmicpc.net/problem/10971
import sys

N = int(input())
board = []
arr = []

min_reuslt = sys.maxsize

for i in range(N):
    board.append(list(map(int, input().split())))

def recursive(start, num):
    global N, min_reuslt
    
    if len(arr) == N:
        if board[start][arr[0]] == 0:
            return
        min_reuslt = min(num + board[start][arr[0]], min_reuslt)
        return
    
    for i in range(N):
        if i in arr:
            continue
        if board[start][i] == 0 and start != i:
            continue
        arr.append(i)
        recursive(i, num + board[start][i])
        arr.pop()
        
recursive(0, 0)

print(min_reuslt)