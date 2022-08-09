# 공유기 설치

N, C = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))
    
arr.sort()

start = 1
end = arr[-1] - arr[0]
A = 0

while start <= end:
    mid = (start + end) // 2 # 4
    cnt = 1
    
    result = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - result >= mid:
            result = arr[i]
            cnt += 1
    
    if cnt < C:
        end = mid - 1
    else:
        A = mid
        start = mid + 1
        
print(A)