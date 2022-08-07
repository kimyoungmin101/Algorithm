N, X = map(int, input().split())
'''
7 2
1 1 2 2 2 2 3
'''
arr = list(map(int, input().split()))
arr.sort()

def bisect_left(target):
    start = 0
    end = len(arr)
    
    while(start <= end):
        mid = (start + end) // 2    
        
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

def bisect_right(target):
    start = 0
    end = len(arr)

    while(start <= end):
        mid = (start + end) // 2    
        
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


print(bisect_right(X) - bisect_left(X))