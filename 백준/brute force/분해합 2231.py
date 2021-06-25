N = (input())

arr = []

for i in range(1, int(N)):
    q = str(i)
    z = i
    for j in range(len(q)):
        z += int(q[j])
    if(z == int(N)):
        arr.append(i)

if(len(arr) == 0 ):
    print(0)
else:
    print(min(arr))

