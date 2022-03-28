N = int(input())

'''
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
'''

import heapq
arr = []
arr = list(map(int, input().split()))

heapq.heapify(arr)

for i in range(N - 1):
    A = list(map(int, input().split()))
    for j in A:
        heapq.heappush(arr, j)
        heapq.heappop(arr)

print(heapq.heappop(arr))