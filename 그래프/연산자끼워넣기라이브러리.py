from itertools import permutations
import sys
N = int(input())

A_arr = list(map(int,input().split()))

solution = ['+', '-', '*', '/']

solution_cnt = list(map(int,input().split()))

new_solution = ''

for i in range(len(solution_cnt)):
    new_solution += (solution_cnt[i] * solution[i])

new_solution = list(map(str, new_solution.strip()))

new_solution = list(set(permutations(new_solution, len(new_solution))))

max_result = -1000000001
min_result = 1000000001

for i in new_solution:
    result = A_arr[0] #1
    for k in range(1, len(A_arr)):
        if i[k-1] == '+':
            result += A_arr[k]
        elif i[k-1] == '-':
            result -= A_arr[k]
        elif i[k-1] == '*':
            result *= A_arr[k]
        else:
            if result < 0:
                result = -result
                result //= A_arr[k]
                result = -result
            else:
                result //= A_arr[k]
        
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    

        # 1 + 2 + 3 / 4 - 5 * 6
        # -4 * 24
print(max_result)
print(min_result)
