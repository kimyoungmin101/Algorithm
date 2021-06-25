N = input()

arr = []

# 각 숫자별로 구분해서 arr에 담아보자
A = ''
for i in range(len(N)):
    if(N[i] != '-' and N[i] != '+'):
        A += N[i]
    else:
        arr.append(int(A))
        arr.append(N[i])
        A = ''

    if(i == (len(N)-1)):
        arr.append(int(A))

# 9+55-50+40
# ->
# ['9', '+', '55', '-', '50', '+', '40']

# 631, - , 342, -, 460

ans = []
Q = 0
while(arr):
    A = arr.pop(0)
    if(len(arr) == 0):
        Q += A
        ans.append(Q)
        break
    if(A == '+'):
        continue
    elif(A == '-'):
        ans.append(Q)
        Q = 0
        ans.append('-')
    else:
        Q += A

Q = ans.pop(0)
for i in ans:
    if(i == '-'):
        continue
    else:
        Q -= i

print(Q)
