N, M = map(int, input().split())
# 4 2
arr = [0 for _ in range(M)] # [0,0]
visited = [False for _ in range(N)] # [False, False, False, False]

def recur(X):
    if X == M:
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return
        for i in arr:
            print(i, end = ' ')
        print()
        return
    
    for i in range(len(visited)):
        arr[X] = i + 1
        recur(X+1)

    return

recur(0)

# 4 2

# 1 1
# 1 2
# 1 3
# 1 4
# 2 1