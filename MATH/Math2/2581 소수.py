M = int(input())
N = int(input())

slist = []

if(M > N):
    print(-1)
else:
    for i in range(M, N + 1):
        if(i == 1 ):
            continue
        if(i == 2):
            slist.append(i)
            continue
        for j in range(2, i):
            if(i % j == 0):
                break
            if(j == (i-1)):
                slist.append(i)
    if(len(slist) == 0):
        print(-1)
    else:
        print(sum(slist))
        print(min(slist))

# https://www.acmicpc.net/problem/2581
