# https://www.acmicpc.net/problem/1025

N, M = map(int, input().split())

board = []
for i in range(N):
    str_a = str(input())
    list_a = list(map(int, str_a.strip()))
    board.append(list_a)

