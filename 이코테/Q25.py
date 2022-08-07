# 실패율

import math

def solution(N, stages):
    answer = []
    
    length = len(stages)
    
    for X in range(1, N+1):
        # 실패율
        count_X = stages.count(X)
        if count_X == 0:
            answer.append([0, X])
        else:
            answer.append([count_X / length, X])
            length -= count_X
            
    answer = sorted(answer, key = lambda X : (-X[0], X[1]))
    
    result = []
    for X in answer:
        result.append(X[1])
        
    return result