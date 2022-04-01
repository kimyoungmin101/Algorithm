# ㅇㅓ두운 길
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
import heapq

N, M = map(int , input().split())

heap = []

parent = [_ for _ in range(N)]

def find(element):
    if element == parent[element]:
        return element
    else:
        return find(parent[element])

def union(X, Y):
    X_parent = find(X)
    Y_parent = find(Y)
    
    if X_parent < Y_parent:
        parent[Y_parent] = X_parent
        return True, parent
    elif X_parent == Y_parent:
        return False, parent
    else:
        parent[X_parent] = Y_parent
        return True, parent

cnt = 0
all_cnt = 0        
for i in range(M):
    A, B, C = map(int, input().split())
    all_cnt += C
    heapq.heappush(heap, [C, A, B])
    
    


while heap:
    C, A, B = heapq.heappop(heap) # 5 2 4
    
    bool_result, parent = union(A,B)
    if bool_result == False:
        continue
    else:
        cnt += C

print(all_cnt - cnt)