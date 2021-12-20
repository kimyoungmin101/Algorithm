from itertools import permutations
from itertools import combinations

L, C = map(int, input().split())
arr_str = list(map(str, input().split()))

word_must = ['a', 'e', 'i', 'o', 'u']

arr_str.sort()
visited = [False for _ in range(len(arr_str))]
arr = [0 for _ in range(L)]

permute = combinations(arr_str, L)

permute = list(permute)
for i in permute:
    result_i = list(i)
    o = 0
    v = 0
    for j in result_i:
        if j in word_must:
            o += 1
        else:
            v += 1
    if o >= 1 and v >= 2:
        result_i = ''.join(result_i)
        print(result_i)


"""
def recur(X):
    if X == L:
        v = 0
        o = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return
        for i in range(len(arr)):
            if arr[i] in word_must:
                o += 1
            else:
                v += 1
        if o >= 1 and v >= 2:
            str_result = "".join(arr)
            print(str_result)
        return
    
    for i in range(len(arr_str)):
        if visited[i] == False:
            visited[i] = True
            arr[X] = arr_str[i]
            recur(X+1)
            visited[i] = False

recur(0)
"""