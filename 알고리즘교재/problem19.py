# 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
import sys
N = int(input())
arr = list(map(int, input().split()))

calculation = list(map(int, input().split()))

max_result = 0
min_result = 10000000
"""def dfs(calcul, add_result, cnt_idx):
    
    if calcul.count(0) == 4:
        max_result = max(add_result, max_result)
        min_result = min(min_result, add_result)
        return
    
    
    return"""

def get_result(idx):
    if idx == 0:
        return '+'
    elif idx == 1:
        return '-'
    elif idx == 2:
        return '*'
    else:
        return '/'
    
max_result = -sys.maxsize -1
min_result = sys.maxsize

def get_sum(calcu):
    result = arr[0]
    for i in range(1, len(arr)):
        if calcu[i-1] == '+':
            result += arr[i]
        elif calcu[i-1] == '-':
            result -= arr[i]
        elif calcu[i-1] == '*':
            result *= arr[i]
        else:
            if result < 0:
                result = -result
                result //= arr[i]
                result = -result
            else:
                result //= arr[i]
    return result

def dfs(calcu, result, sum_cal):
    global max_result
    global min_result
    
    if len(result) == sum_cal:
        result_sum = get_sum(result)
        max_result = max(result_sum, max_result)
        min_result = min(min_result, result_sum)
        
        return
    
    for i in range(len(calcu)):
        if calcu[i] != 0:
            calcu[i] -= 1
            result.append(get_result(i))
            dfs(calcu, result, sum_cal)
            result.pop()
            calcu[i] += 1
    
    return

sum_cal = sum(calculation)
dfs(calculation, [], sum_cal)

print(max_result)
print(min_result)