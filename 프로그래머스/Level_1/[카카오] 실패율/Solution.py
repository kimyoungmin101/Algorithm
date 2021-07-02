def solution(N, stages):
    answer = [0 for _ in range(N)]
    stages.sort()
    lenA = len(stages)
    
    for i in range(N):
        countA = stages.count(i+1) #1
        if(lenA == 0):
            answer[i] = [0, i+1]
        else:
            answer[i] = [(countA / lenA), i+1]
        lenA -= countA
    
    result = sorted(answer, key = lambda x : x[0], reverse = True)
    
    
    qwe = []
    for i in result:
        qwe.append(i[1])
        
    return qwe
