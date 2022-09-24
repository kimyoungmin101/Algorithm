# https://school.programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    answer = 0
    
    dic = {}
    for i in range(len(info)):
        dic[i] = []
    
    for edge in edges:
        X, Y = edge # 출발, 도착
        dic[X].append([Y, info[Y]]) # 도착, 늑대인지 양인지 / 0은양, 1은 늑대
        
    stack = [[1,0,[0]]] # 양의수, 늑대의수, 방문한 visited
        
    while stack:
        X, Y, visited = stack.pop() # 1,0,[0]
        
        for q in visited:
            for i in dic[q]:
                A, B = i # 1,0 # 1번에 양이 있다.
                if A not in visited:
                    if B == 0: #양이면
                        new_visit = visited.copy()
                        new_visit.append(A)
                        stack.append([X+1, Y,new_visit])
                        answer = max(X+1, answer)
                    else:
                        if X > (Y + 1):
                            new_visit = visited.copy()
                            new_visit.append(A)
                            stack.append([X,Y+1,new_visit])
                    
    if answer == 0:
        return 1
    return answer