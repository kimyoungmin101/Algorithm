N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))

dp = [0 for _ in range(len(arr))]

# 1) 0 0 0 0 0 0 0
# 2) 0 0 0 0 0 0 0
# 3) 0 0 10 0 0 0 0
# 4) 0 0 10 30 0 0 0
# 5) 0 0 10 30 30 0 0
# 6) 0 0 10 30 30 45 45
# 7) 0 0 10 30 30 45 45

# 0 0 10 20 0 20 0
max_result = 0

for i in range(len(arr)):
    if (arr[i][0] + i - 1) >= len(arr):
        arr[i] = [1, 0]

def find_get(arr_i, arr_list, start_idx, sum_result): # 5 50
    global max_result
    sum_result += arr_i[1]
    new_arr = arr_list[start_idx:].copy() # [1, 10], [2, 20], [3, 30], [0, 0], [0, 0]

    if len(new_arr) == 0:
        max_result = max(max_result, sum_result)
        return

    for i in range(len(new_arr)):
        find_get(new_arr[i], new_arr, i + new_arr[i][0], sum_result) # 1 10
    
    return

for i in range(len(arr)):
    find_get(arr[i], arr, i + arr[i][0], 0)

print(max_result)