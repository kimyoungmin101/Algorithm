import sys

T = int(sys.stdin.readline())

def cal(N):
    arr = [[1,0], [0,1]]
    for i in range(2, N + 1):
        arr.append([arr[i-1][1], arr[i-1][0] + arr[i-1][1]])
    print(arr[N][0], arr[N][1])
    
for i in range(T):
    N = int(sys.stdin.readline())
    cal(N)

