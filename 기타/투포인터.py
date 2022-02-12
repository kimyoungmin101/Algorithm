# 알고리즘 교재 P472

data = [1,2,3,2,5,2,1,3,24,1,5,21,1,3,2,4,5,3,2,21,2,1,3,4,5,6,1,2,5,3,4,5]
M = 5
'''
부분 합이 5인 부분의 count를 리턴하는 알고리즘을 짜라
'''

start, end = 0, 0
cnt = 0
while start < len(data) + 1 and end < len(data) + 1:
    ans = sum(data[start:end])
    if ans == M:
        end += 1
        cnt += 1
    elif ans < M:
        end += 1
    else:
        start += 1

print(cnt)


n = len(data)
m = 5

count = 0
interval_sum = 0
end = 0

# data = [1,2,3,2,5,2]
for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)
