# 만들 수 없는 금액
N = int(input())

arr = list(map(int, input().split()))

value = 1
arr.sort()

'''
5
3 2 1 1 9
'''

for i in arr:
    if value < i:
        break
    value += i

print(value)

# 1 1 2 3 9
