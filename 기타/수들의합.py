'''
10 5
1 2 3 4 2 5 3 1 1 2
'''

N, M = map(int , input().split())
arr = list(map(int, input().split()))

end = 0
sum_value = 0
cnt = 0

for start in range(len(arr)):
    while end < N and sum_value < M:
        sum_value += arr[end]
        end += 1
    
    if sum_value == M:
        cnt += 1
    
    sum_value -= arr[start]

print(cnt)