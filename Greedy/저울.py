N = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1

for i in arr:
    if i > target:
        break

    target += i

print(target)
'''
7
3 1 6 2 7 30 1
'''