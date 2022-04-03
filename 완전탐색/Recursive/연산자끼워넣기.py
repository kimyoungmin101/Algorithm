# https://www.acmicpc.net/problem/14888

N = int(input())
A = list(map(int , input().split()))

result = list(map(int, input().split()))

min_result = 1000000001
max_result = -1000000001

def recursive(arr, res, ans, idx):
    global max_result
    global min_result
    
    if sum(res) == 0:
        max_result = max(ans, max_result)
        min_result = min(ans, min_result)
        return
    
    if res[0] >= 1:
        res[0] -= 1
        AB = ans + arr[idx]
        recursive(arr, res, AB, idx + 1)
        res[0] += 1
    
    if res[1] >= 1:
        res[1] -= 1
        AB = ans - arr[idx]
        recursive(arr, res, AB, idx + 1)
        res[1] += 1
    
    if res[2] >= 1:
        res[2] -= 1
        AB = ans * arr[idx]
        recursive(arr, res, AB, idx + 1)
        res[2] += 1
    
    if res[3] >= 1:
        res[3] -= 1
        if ans < 0 and arr[idx] >= 0:
            ans = -ans
            AB = ans // arr[idx]
            AB = -AB
        else:
            AB = ans // arr[idx]
        
        recursive(arr, res, AB, idx + 1)
        res[3] += 1
        
        
a_zero = A[0]
A = A[1:]

recursive(A, result, a_zero, 0)

print(max_result)
print(min_result)

'''
3
1 2 1
0 1 0 1
'''