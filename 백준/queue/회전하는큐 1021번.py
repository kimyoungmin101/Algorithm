import sys
import collections

N, M = map(int, sys.stdin.readline().split())

que = [0] * N
que = collections.deque(que)

A = list(map(int, sys.stdin.readline().split())) #지민이가 뽑아내려는 카드의 위치

for i in range(len(que)+1):
    que[i-1] = i
    
count = 0
popnum = 0

for i in A:
    if(que[0] == i):
        que.popleft()
    else:
        if que.index(i) > (len(que) // 2):
            while(que[0] != i):
                que.rotate(1)
                count += 1
            que.popleft()
        else:
            while(que[0] != i):
                que.rotate(-1)
                count += 1
            que.popleft()

print(count)


            
        
    
