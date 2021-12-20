def solution(n, lost, reserve):
    answer = 0
    list_answer = set(lost) - set(reserve)
    reserve_answer = set(reserve) - set(lost)
    reserve_answer = list(reserve_answer)
    list_answer = list(list_answer)
    list_answer.sort()
    reserve_answer.sort()
    
    #이렇게 중복된 숫자를 제거 해줄 수 있다. set활용 중요 !!
    
    while(reserve_answer):
        A = reserve_answer.pop(0)
        
        if(A - 1) in list_answer:
            list_answer.remove(A - 1)
            continue
        elif(A + 1) in list_answer:
            list_answer.remove(A + 1)
            continue
        if(len(lost) == 0):
            return n
    
    return n - len(list_answer)
