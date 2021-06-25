import sys

N = int(sys.stdin.readline())


def vps(A):
    stack = []
    for i in range(len(A)):
        stack.append(A[i])
        while(len(stack) >= 2 and stack[len(stack)-1] == ')' and stack[len(stack)-2] == '('):
            stack.pop()
            stack.pop()
    if(len(stack) == 0):
        return 'YES'
    else:
        return 'NO'

for i in range(N):
    A = str(input())
    print(vps(A))
