import sys
import collections

N = int(sys.stdin.readline())


for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    arrA = [0] * arr[0] # 리스트!!
    arrA[arr[1]] = arr[0]

    importA = list(map(int, sys.stdin.readline().split())) # 중요도

    arrA = collections.deque(arrA)
    importA = collections.deque(importA)

    count = 0
    while(arrA):
        maxI = max(importA)
        if(maxI == importA[0]):
            count += 1
            V = importA.popleft()
            Q = arrA.popleft()
            if(Q != 0):
                print(count)
                break
        else:
            importA.rotate(-1)
            arrA.rotate(-1)
