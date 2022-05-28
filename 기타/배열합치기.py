# https://www.acmicpc.net/problem/11728

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
len_arr = len(A) + len(B)

len_A = len(A)
len_B = len(B)

arr = []

start_one = 0
start_two = 0

for i in range(len_arr):
    if len_A <= start_one:
        arr.append(B[start_two])
        start_two += 1
        continue
    if len_B <= start_two:
        arr.append(A[start_one])
        start_one += 1
        continue
    
    if A[start_one] < B[start_two]:
        arr.append(A[start_one])
        start_one += 1
    else:
        arr.append(B[start_two])
        start_two += 1

for i in arr:
    print(i, end = " ")