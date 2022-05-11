# https://www.acmicpc.net/problem/14888
import sys
N = int(input())
A = list(map(int, input().split()))
# add, minus, ax, divide = map(int, input().split())
answer = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001

def recursive(cnt_arr, cnt_answer, result):
    global max_result, min_result
    
    if sum(cnt_answer) == 0:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if cnt_answer[0] >= 1: # 덧셈
        AB = result + A[cnt_arr]
        cnt_answer[0] -= 1
        recursive(cnt_arr + 1, cnt_answer, AB)
        cnt_answer[0] += 1
        
    if cnt_answer[1] >= 1:
        AB = result - A[cnt_arr]
        cnt_answer[1] -= 1
        recursive(cnt_arr + 1, cnt_answer, AB)
        cnt_answer[1] += 1
        
    if cnt_answer[2] >= 1:
        AB = result * A[cnt_arr]
        cnt_answer[2] -= 1
        recursive(cnt_arr + 1, cnt_answer, AB)
        cnt_answer[2] += 1
        
    if cnt_answer[3] >= 1:
        if result < 0 and A[cnt_arr] >= 0:
            AB = -result
            AB //= A[cnt_arr]
            AB = -AB
        else:
            AB = result // A[cnt_arr]
        cnt_answer[3] -= 1
        recursive(cnt_arr + 1, cnt_answer, AB)
        cnt_answer[3] += 1

recursive(1, answer, A[0])

print(max_result, min_result)
