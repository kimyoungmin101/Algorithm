import sys

N, C = map(int, (input().split()))
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

# [1, 2, 4, 8, 9]

result = 0
start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    next = house[0]
    for i in range(1, len(house)):
        if next + mid <= house[i]:
            next = house[i]
            cnt += 1
            
    if cnt < C:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        

print(result)