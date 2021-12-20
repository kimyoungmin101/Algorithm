N, M = map(int, input().split())

arr = []

for i in range(N): 
    arr.append(int(input()))

arr.sort()

# [1, 2, 4, 8, 9]
min_arr = min(arr) # 1
max_arr = max(arr) # 9

max_result = 0
