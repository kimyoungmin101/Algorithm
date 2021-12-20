N = int(input())

arr = []

for i in range(N):
    A = input()
    arr.append(A)

arr = sorted(arr, key = lambda x : (len(x), x))

ans = []

for i in arr:
    if(i not in ans):
        ans.append(i)
        print(i)
