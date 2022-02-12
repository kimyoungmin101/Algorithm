# 알고리즘 교재 P397 Q43
import heapq

N,M = map(int ,input().split())

arr = [[0 for _ in range(N)] for _ in range(N)]

heap = []

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

def find_parent(W):
    if parent[W] == W:
        return W
    else:
        return find_parent(parent[W])


for i in range(M):
    X, Y, Z = map(int, input().split())
    heapq.heappush(heap, [Z, X, Y])



all_cnt = 0
union_cnt = 0

while heap:
    result = heapq.heappop(heap)
    all_cnt += result[0]
    if union(result[1], result[2]):
        union_cnt += result[0]
        continue
    

print(all_cnt - union_cnt)
'''
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
'''