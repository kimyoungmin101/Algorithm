# 행성 터널
'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''
import heapq

N = int(input())

A_arr = []
B_arr = []
C_arr = []

for i in range(N):
    A, B, C = map(int , input().split())
    
    A_arr.append([A, i])
    B_arr.append([B, i])
    C_arr.append([C, i])    
    
A_arr.sort()
B_arr.sort()
C_arr.sort()

heap = []

for i in range(1, len(A_arr)):
    A = A_arr[i]
    B = B_arr[i]
    C = C_arr[i]
    
    prev_A = A_arr[i-1]
    prev_B = B_arr[i-1]
    prev_C = C_arr[i-1]
    
    A_value = A[0] - prev_A[0]
    B_value = B[0] - prev_B[0]
    C_value = C[0] - prev_C[0]
    
    heapq.heappush(heap, [A_value, A[1], prev_A[1]])
    heapq.heappush(heap, [B_value, B[1], prev_B[1]])
    heapq.heappush(heap, [C_value, C[1], prev_C[1]])

parent = [_ for _ in range(N)]

def find(element):
    if element == parent[element]:
        return element
    else:
        return find(parent[element])

def union(dx, dy):
    parent_X = find(dx)
    parent_Y = find(dy)
    
    if parent_X < parent_Y:
        parent[parent_Y] = parent_X
        return True
    elif parent_X == parent_Y:
        return False
    else:
        parent[parent_X] = parent_Y
        return True
    
weight = 0

while heap:
    value, X, Y = heapq.heappop(heap)
    
    if union(X,Y):
        weight += value

print(weight)