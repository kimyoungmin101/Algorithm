N, M = 10, 19
arr = [1,3,5,7,9,11,13,15,17,19]

start = 0
end = len(arr) - 1
answer = 0

while start <= end:
    
    mid = (start + end) // 2
    
    if arr[mid] == M:
        answer = mid
        break
    elif arr[mid] > M:
        end = mid -1
    else:
        start = mid + 1
    
print(answer)        