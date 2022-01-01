from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
arr.sort()

list_combi = list(combinations(arr, 2))

for a, b in list_combi:
    if a != b:
        result += 1
print(result)
'''
8 5
1 5 4 3 2 4 5 2
'''
