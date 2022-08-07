N = int(input())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = len(arr) - 1

result = -1

while start <= end:
    mid = (start + end) // 2
    
    if mid == arr[mid]:
        result = mid
        break
    elif mid < arr[mid]:
        end = mid - 1
    else:
        start = mid + 1
        
print(result)

'''
7
-3 -2 2 8 9 13 15
'''