T = int(input())

for i in range(T):
    N = int(input())
    dic = {}
    for j in range(N):
        listQ = list(map(str, input().split()))
        if(listQ[1] not in dic):
            dic[listQ[1]] = 2
        else:
            dic[listQ[1]] += 1
    ans = list(dic.values())
    result = 1
    for k in ans:
        result *= k
    print(result - 1)
    
