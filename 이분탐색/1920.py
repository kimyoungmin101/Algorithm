# 수 찾기


        
N = int(input())
arr = list(map(int, input().split()))

M = int(input())
arr_two = list(map(int, input().split()))
arr.sort()

def binary_search(target):
    start = 0
    end = len(arr) - 1
    
    while(start <= end):
        
        mid = (start + end) // 2
        
        if(arr[mid] < target):
            start = mid + 1
        elif(arr[mid] == target):
            return True
        else:
            end = mid - 1
    
    return False

for value in arr_two:
    if binary_search(value):
        print(1)
    else:
        print(0)