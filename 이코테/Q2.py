# 곱하기 혹은 더하기

N = str(input())
num = int(N[0])
for i in range(1, len(N)):
    A = num + int(N[i])
    B = num * int(N[i])
    
    if A > B:
        num = A
    else:
        num = B

print(num)