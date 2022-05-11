# https://www.acmicpc.net/problem/1174
import sys
arr = list()
result = set()

N = int(input())

def recursive():
    ans = "".join(list(map(str, arr)))
    if ans != '':
        result.add(int(ans))
    
    for i in range(0, 10):
        if len(arr) == 0:
            arr.append(i)
            recursive()
            arr.pop()
        elif arr[-1] > i:
            arr.append(i)
            recursive()
            arr.pop()
recursive()
result = list(result)
result.sort()

try:
    print(result[N-1])
except:
    print(-1)

