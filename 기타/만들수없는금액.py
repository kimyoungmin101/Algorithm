
'''
5
3 2 1 1 9
'''

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
target = 1

for X in arr:
    if target < X:
        break
    target += X

print(target)