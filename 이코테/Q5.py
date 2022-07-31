# 볼링공 고르기 

N, M = map(int, input().split())
arr = list(map(int, input().split()))

'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

1 2 3
1 2 3 4 5
7 + 5 + 4 + 2
'''

arr.sort()

value = arr[0]
value_cnt = 1

cnt_all = len(arr)
result = 0

for i in range(1, len(arr)):
    if arr[i] == value:
        value_cnt += 1
    else:
        value = arr[i]
        cnt_all -= value_cnt
        result += (cnt_all * value_cnt)
        value_cnt = 1

print(result)