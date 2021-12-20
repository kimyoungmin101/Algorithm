def solution(genres, plays):
    answer = []
    
    for i in range(len(genres)):
        A = [0,0,0]
        A[0] = genres[i]
        A[1] = plays[i]
        A[2] = i
        answer.append(A)
    answer = sorted(answer, key = lambda x : (x[0], x[1], -x[2]), reverse = True)
    dic = {}
    
    print(answer)
    
    for i in answer:
        if(i[0] not in dic):
            dic[i[0]] = i[1]
        else:
            dic[i[0]] += i[1]
    
    dics = []
    for i in dic.items():
        dics.append([i[0], i[1]])
        
    dics = sorted(dics, key = lambda x : x[1], reverse = True)
    
    ans = []
    
    while(dics):
        cnt = 0
        A = dics.pop(0)
        for i in range(len(answer)):
            if(A[0] == answer[i][0] and cnt < 2):
                ans.append(answer[i][2])
                cnt += 1
                
    return ans
