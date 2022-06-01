'''
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''

from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
arr = list(map(int, input().split()))

A = bisect_left(arr, M)
B = bisect_right(arr, M)

if B - A == 0:
    print(-1)
else:
 print(B - A)