lists = []
for i in range(1, 10001):
    lists.append(i)

def selfin():
    for i in range(1, 10001):
        ans = 0
        ans += i
        Q = i
        while(Q > 0):
            A = Q % 10
            ans += A
            Q = Q / 10
            Q = int(Q)
        if(ans in lists):
            lists.remove(ans)
    return lists
    

V = selfin()
for i in V:
    print(i)
    
