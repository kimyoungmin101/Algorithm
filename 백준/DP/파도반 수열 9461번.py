N = int(input())

def DP(A):
    arr = [0, 1, 1, 1]
    if(A >= 4):
        for i in range(4, A+1):
            arr.append(arr[i-2] + arr[i-3])
    return arr[A]

for i in range(N):
    A = int(input())
    print(DP(A))
