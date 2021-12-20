from sys import stdin, stdout

K, N = map(int, stdin.readline().split())
arr = []

for i in range(K):
    arr.append(int(stdin.readline()))


start = 1
end = max(arr) # 802

while(start <= end):
    mid = (start + end) // 2 # 401
    sum_result = 0
    
    for i in arr:
        sum_result += (i // mid)

    if(sum_result >= N):
        start = mid + 1
    else:
        end = mid - 1

print(end)