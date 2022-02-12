# https://www.acmicpc.net/problem/2887

'''
알고리즘 분류
그래프 이론
정렬
최소 스패닝 트리
'''
from re import X
import sys
import heapq

N = int(input())

graph = []

X_arr = []
Y_arr = []
Z_arr = []

for i in range(N):
    NEW_A = list(map(int, input().split()))
    X_arr.append([NEW_A[0], i])
    Y_arr.append([NEW_A[1], i])
    Z_arr.append([NEW_A[2], i])

X_arr.sort()
Y_arr.sort()
Z_arr.sort()

parent = [_ for _ in range(N)]

def union(A, B):
    A_parent = find_parent(A)
    B_parent = find_parent(B)

    if A_parent < B_parent:
        parent[B_parent] = A_parent
        return True
    elif A_parent == B_parent:
        return False
    else:
        parent[A_parent] = B_parent
        return True

def find_parent(X):
    if parent[X] == X:
        return X
    else:
        return find_parent(parent[X])

heap = []

for i in range(1, N):
    heapq.heappush(heap, [X_arr[i][0] - X_arr[i-1][0], X_arr[i][1], X_arr[i-1][1]])
    heapq.heappush(heap, [Y_arr[i][0] - Y_arr[i-1][0], Y_arr[i][1], Y_arr[i-1][1]])
    heapq.heappush(heap, [Z_arr[i][0] - Z_arr[i-1][0], Z_arr[i][1], Z_arr[i-1][1]])

result_cnt = 0
while(heap):
    A = heapq.heappop(heap)
    if union(A[1], A[2]):
        result_cnt += A[0]

print(result_cnt)