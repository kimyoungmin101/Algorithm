N = int(input())

nlist = list(map(int, input().split()))


count = 0

for i in nlist:
    if(i == 1):
        continue
    if(i == 2):
        count += 1
        continue
    for j in range(2, i):
        if(i % j == 0):
            break
        if(j == (i-1)):
            count += 1

print(count)

# https://www.acmicpc.net/problem/1978
