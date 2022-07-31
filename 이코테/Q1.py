# 모험가 길드

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = []
new_arr = []
cnt = 0

for i in arr:
    new_arr.append(i)
    if i <= len(new_arr):
        cnt += 1
        new_arr = []

print(cnt)