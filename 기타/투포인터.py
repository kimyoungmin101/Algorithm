# 알고리즘 교재 P472


M = 5

data = [1,2,3,2,5]
'''
부분 합이 5인 부분의 count를 리턴하는 알고리즘을 짜라
'''

end = 0
interval_sum = 0

cnt = 0

for start in range(len(data)):
    while interval_sum < M and end < len(data):
        interval_sum += data[end]
        end += 1
    
    if interval_sum == M:
        cnt += 1
    
    interval_sum -= data[start]

print(cnt)