import sys
import collections

N = int(sys.stdin.readline())

arr = collections.deque([])

for i in range(1, N+1):
    arr.append(i)

while(len(arr) != 1):
    arr.popleft()
    arr.rotate(-1)    

print(arr[0])
