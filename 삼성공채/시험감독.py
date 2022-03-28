N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for i in range(len(A)):
    A[i] -= B
    cnt += 1
    if A[i] < 0:
        A[i] = 0

for i in range(len(A)):
    X, Y = divmod(A[i], C)
    cnt += X
    if Y > 0:
        cnt += 1
        
print(cnt)
# 1 2 3