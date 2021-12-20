import sys
import collections
N = int(sys.stdin.readline())

ans = collections.deque([])

def push(X):
    ans.append(X)

def popp():
    if(len(ans) >= 1):
        Q = ans.popleft()
        print(Q)
    else:
        print(-1)

def size():
    print(len(ans))


def isEmpty():
    if(len(ans) == 0):
        print(1)
    else:
        print(0)
    
def front():
    if(len(ans) >= 1):
        print(ans[0])
    else:
        print(-1)

def back():
    if(len(ans) >= 1):
        print(ans[-1])
    else:
        print(-1)

arr = []

for i in range(N):
    listN = list(map(str, sys.stdin.readline().split()))
    arr.append(listN)

for A in arr:
    if(A[0] == 'push'):
        push(A[1])
    elif(A[0] == 'pop'):
        arr = popp()
    elif(A[0] == 'size'):
        size()
    elif(A[0] == 'empty'):
        isEmpty()
    elif(A[0] == 'front'):
        front()
    else:
        back()
    
