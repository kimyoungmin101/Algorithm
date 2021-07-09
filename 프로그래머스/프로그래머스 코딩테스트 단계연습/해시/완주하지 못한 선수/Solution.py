def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    setpart = set(participant)
    setcom = set(completion)
    
    resultset = setpart - setcom
    resultset = list(resultset)
    
    if(len(resultset) != 0):
        return resultset[0]
    else:
        for i in range(len(completion)):
            if(completion[i] != participant[i]):
                return participant[i]
        return participant[-1]
