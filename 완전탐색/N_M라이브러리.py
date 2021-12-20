from itertools import permutations

N, M = map(int, input().split()) # 4 2

arr = [i for i in range(1, N+1)]

permu = list(permutations(arr, M))


for i in permu:
    arr_i = list(map(str,i))
    result = ' '.join(arr_i)
    print(result)
