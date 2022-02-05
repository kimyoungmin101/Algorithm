# 알고리즘 교재 P388
'''
1. 화성 탐사
난이도
중
풀이 시간
40분
시간 제한
1초
메모리 제한
128MB
기출
ACM-ICPC
A. 📜 문제
당신은 화성 탐사 기계를 개발하는 프로그래머다. 그런데 화성은 에너지 공급원을 찾기가 힘들다. 그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 한다.

화성 탐사 기계가 존재하는 공간은 N x N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용(에너지 소모량)이 존재한다. 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N - 1][N - 1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하라. 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.

a. 입력 조건
첫째 줄에 테스트 케이스의 수 T(1 <= T <= 10)가 주어진다.
매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어진다.
2 <= N <= 125
이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분한다.
0 <= 각 칸의 비용 <= 9
c. 출력 조건
각 테스트 케이스마다 [0][0]의 위치에서 [N - 1][N - 1]의 위치로 이동하는 최소 비용을 한 줄에 하나씩 출력한다.
d. 테스트 케이스
입력 예시


3  
3  
5 5 4  
3 9 1  
3 2 7  
5  
3 7 2 0 1  
2 8 0 9 1  
1 2 1 8 1  
9 8 9 2 0  
3 6 5 1 5  
7  
9 0 5 1 1 5 3  
4 1 2 1 6 5 3  
0 7 6 1 6 8 5  
1 1 7 8 3 2 3  
9 4 0 7 6 4 1  
5 8 3 2 4 8 3  
7 4 8 4 8 3 4

'''

import heapq
import sys
from collections import deque

N = int(input())
for i in range(N):
    M = int(input())
    arr = []
    for j in range(M):
        arr.append(list(map(int, input().split())))
    
    graph = [[sys.maxsize for _ in range(M)] for _ in range(M)]
    graph[0][0] = arr[0][0]
    queue = deque([[0,0]])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        X, Y = queue.popleft()
        for k in range(4):
            real_X = X + dx[k]
            real_Y = Y + dy[k]

            if real_X < 0 or real_Y < 0 or real_X >= M or real_Y >= M:
                continue
            
            if graph[real_X][real_Y] > graph[X][Y] + arr[real_X][real_Y]:
                queue.append([real_X, real_Y])
                graph[real_X][real_Y] = graph[X][Y] + arr[real_X][real_Y]
    print(graph[-1][-1])
    