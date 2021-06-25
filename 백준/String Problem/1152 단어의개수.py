A, B = map(str, input().split())


C = ''
D = ''
for i in range(len(A)):
    C += A[len(A) -i - 1]
    D += B[len(B) -i - 1]


C = int(C)
D = int(D)

if(C > D):
    print(C)
else:
    print(D)
