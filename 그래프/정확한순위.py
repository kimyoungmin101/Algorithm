# 교재 p385
import sys
from turtle import st
cnt = 0

N, M = map(int, input().split()) # 학생수, 비교한 횟수
students = [[sys.maxsize for _ in range(N)] for _ in range(N)]
for _ in range(M):
    X, Y = map(int,input().split())
    X -= 1
    Y -= 1
    students[X][Y] = 1
    
for i in range(N):
    students[i][i] = 0
    
visite_arr = [[] for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            students[a][b] = min(students[a][b], students[a][k] + students[k][b])

result = 0
for i in range(N):
    count = 0
    for j in range(N):
        if students[i][j] != sys.maxsize or students[j][i] != sys.maxsize:
            count += 1
    if count == N:
        result += 1
print(result)
'''
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''