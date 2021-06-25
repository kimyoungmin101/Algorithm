N = int(input())

arr = list(map(int, input().split()))
PDP = [1] * N # 순서가 plus 일때 저장할 Dp
MDP = [0] * N # 순서가 minus 일떄 저장할 Dp

max = 0

for i in range(N):
    for j in range(i):
        if(i >= 1 and arr[i] > arr[j] and max < (PDP[j] + 1)):
            max = PDP[j] + 1
            PDP[i] = max
    max = 0

arr.reverse()

for i in range(N):
    for j in range(i):
        if(i >= 1 and arr[i] > arr[j] and max < (MDP[j] + 1)):
            max = MDP[j] + 1
            MDP[i] = max
    max = 0

MDP.reverse()

max = 0

for i in range(N):
    A = MDP[i] + PDP[i]
    if( A > max ):
        max = A

print(max)
