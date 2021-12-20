from itertools import permutations

arr = [1,2,3,4]
arr = list(map(str, arr))


ans = set([])
for i in range(len(arr)):
    A = list(map("".join, permutations(arr, i+1)))
    for j in A:
        ans.add(j)

ans = list(ans)

ans = list(map(int, ans))
ans.sort()

print(ans)

