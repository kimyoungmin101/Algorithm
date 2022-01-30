N, M = map(int, input().split())

checked = [False] * (N+1)
arr = [0] * (M + 1)

#r = m

def recur(r):
    if(r == M+1):
        for i in range(1, len(arr)):
            print(arr[i], end=" ")
        print()
        return
    for i in range(1, N+1):
        if(checked[i] == False):
            checked[i] = True
            arr[r] = i
            recur(r+1)
            checked[i] = False        

recur(1)
