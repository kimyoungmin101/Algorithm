N, M = map(int, input().split())


arr = [0] * ( M + 1 )


def recur(r):
    if(r == M+1):
        for i in range(1, len(arr)):
            print(arr[i], end =" ")
        print()
        return
    for i in range(1, N+1):
        arr[r] = i
        recur(r+1)


recur(1)
