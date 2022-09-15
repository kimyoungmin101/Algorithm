# https://www.acmicpc.net/problem/15591

from collections import deque
import sys

N, Q = map(int, input().split())

dic = {}

for i in range(N-1):
    A, B, C = map(int , input().split())    
    if A not in dic:
        dic[A] = [[B, C]]
    else:
        dic[A].append([B, C])
    if B not in dic:
        dic[B] = [[A, C]]
    else:
        dic[B].append([A, C])


for i in range(Q):
    U, D = map(int, input().split()) # 유사도, 동영상 번호
    
    visit = [False for _ in range(N+1)]
    
    weight = [sys.maxsize for _ in range(N+1)]
    weight[0] = 0
    weight[D] = 0
    
    queue = deque([])
    visit[D] = True
    
    for a in dic[D]:
        weight[a[0]] = a[1]
        queue.append(a)
    
    while queue:
        A, B = queue.popleft() # 다음 동영상, 유사도 크기 # [2, 3]
        if visit[A]:
            continue
        visit[A] = True
        
        for next_idx, d_size in dic[A]: # 다음 동영상, 유사도 크기 / 1,3 / 3,2 / 4,4
            if visit[next_idx]:
                continue
            weight[next_idx] = min(weight[A], d_size)
            queue.append([next_idx, d_size])
    
    cnt = 0
    
    for w in weight:
        if w >= U:
            cnt += 1
    
    print(cnt)