import sys
N = int(sys.stdin.readline())

stack = []

def push(N):
    stack.append(N)
    return stack

def top():
    if(len(stack) == 0):
        return -1
    else:
        return stack[-1]

def size():
    return len(stack)

def empty():
    if(len(stack) == 0):
        return 1
    else:
        return 0

def pop():
    if(len(stack) == 0):
        return -1
    else:
        A = stack.pop()
        return A
    
for i in range(N):
    A = list(map(str, sys.stdin.readline().rstrip().split()))
    if(A[0] == 'push'):
        push(A[1])
    elif(A[0] == 'top'):
        print(top())
    elif(A[0] == 'size'):
        print(size())
    elif(A[0] == 'empty'):
        print(empty())
    elif(A[0] == 'pop'):
        print(pop())
