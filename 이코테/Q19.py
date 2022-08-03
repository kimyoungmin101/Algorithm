# 연산자 끼워넣기

import sys

max_value = 0
min_value = sys.maxsize

N = int(input())
A = list(map(int, input().split()))

ans = list(map(int, input().split())) # 더하기 , 빼기, 꼽하기, 나누기
# P, M, G, D

def dfs(next_ans, value, idx):
    global max_value, min_value
        
    P, M, G, D = next_ans
    if next_ans.count(0) == len(next_ans):
        max_value = max(value, max_value)
        min_value = min(value, min_value)
        return
    
    if P >= 1: # PLUS
        next_ans[0] -= 1
        dfs(next_ans, value + A[idx], idx + 1)
        next_ans[0] += 1
    if M >= 1: # MINUS
        next_ans[1] -= 1
        dfs(next_ans, value - A[idx], idx + 1)
        next_ans[1] += 1
    if G >= 1: # MUTLI
        next_ans[2] -= 1
        dfs(next_ans, value * A[idx], idx + 1)
        next_ans[2] += 1
    if D >= 1: # DIVIDE 
        new_value = value
        if value < 0:
            new_value = -new_value
            new_value //= A[idx]
            new_value = -new_value
        else:    
            new_value //= A[idx]
        next_ans[3] -= 1
        dfs(next_ans, new_value, idx + 1)
        next_ans[3] += 1

dfs(ans, A[0], 1)

print(max_value)
print(min_value)