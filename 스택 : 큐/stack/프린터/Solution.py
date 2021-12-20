def solution(priorities, location):
    answer = 0
    ans = []

    for i in range(len(priorities)):
        if(i == location):
            priorities[i] = [priorities[i], True]
        else:
            priorities[i] = [priorities[i], False]
    
    def rotate(l, n):
        return l[n:] + l[:n]

    def maxlen(l):
        maxle = max(l, key = lambda x : x[0])
        maxle = maxle[0]
        return maxle
        
    while(priorities):
        A = priorities[0][0] # 2
        if(len(priorities) >= 2):
            reA = priorities[1:]
            Q = maxlen(reA) # 4
        else:
            ans.append(priorities.pop(0))
            break
        if(A >= Q):
            ans.append(priorities.pop(0))
        else:
            priorities = rotate(priorities, 1)
            
    for i in range(len(ans)):
        if(ans[i][1] == True):
            return i + 1
