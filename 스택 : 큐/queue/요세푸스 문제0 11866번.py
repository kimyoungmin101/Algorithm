import sys
import collections

N, K = map(int, sys.stdin.readline().split())

arr = collections.deque([])
ans = []

for i in range(1, N+1):
    arr.append(i)


while(arr):
    arr.rotate(-K+1)
    ans.append(arr.popleft())

print('<', end="")
for i in ans:
    if(i == ans[-1]):
        print(i, end="")
    else:
        print(i, end=", ")
print('>')
