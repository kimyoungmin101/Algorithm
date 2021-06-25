import sys


while(True):
    S = input()
    stack = []
    if S == '.':
        break
    else:
        for j in S:
            if(j == '(' or j == ')' or j == '[' or j == ']'):
                stack.append(j)
    ans = []

    if(len(stack) == 0):
        print('yes')
        continue

    while(stack):
        A = stack.pop(0)
        if(len(ans) == 0) and (A == ']' or A == ')'):
            ans.append('no')
            break
        if(len(ans) == 0):
            ans.append(A)
            continue
        if(A == '(' or A == '['):
            ans.append(A)
        elif(A == ')'):
            if(ans[-1] == '('):
                ans.pop()
            else:
                break
        elif(A == ']'):
            if(ans[-1] == '['):
                ans.pop()
            else:
                break
    if(len(ans) == 0):
        print('yes')
    else:
        print('no')

