def solution(progresses, speeds):
    answer = []
    res = []
    real = []
    N = []
    while(progresses):
        A = progresses.pop(0)
        B = speeds.pop(0)
        
        ans = 100 - A # 7
        if((ans % B) != 0):
            result = (ans // B) + 1
        else:
            result = (ans // B)
        
        answer.append(result)
        
    for i in range(len(answer)):
        if(i < (len(answer) -1 ) and answer[i] > answer[i + 1]):
            answer[i + 1] = answer[i]
    
    for i in answer:
        if(i not in real):
            real.append(i)
    
    for i in real:
        N.append(answer.count(i))
    
    return N
