N, M = map(int, input().split())


arr = [0] * ( M + 1 )

def recur(K):
    if(K == (M+1)):
        A = arr[1:]
        ans = A[0]

        for i in A[1:]:
            if(i < ans):
                return
            else:
                ans = i

        for i in range(len(A)):
            print(A[i], end =" ")
        print()
        return
    for i in range(1, N+1):
        arr[K] = i
        recur(K+1)

recur(1)
        
        
