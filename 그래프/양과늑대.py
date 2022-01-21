# 코딩테스트 연습 2022 KAKAO BLIND RECRUITMENT 양과 늑대
# https://programmers.co.kr/learn/courses/30/lessons/92343

def solution(info, edges):
    dic_arr = {}
    
    for i in range(len(info)):
        dic_arr[i] = []
    
    for i in edges:
        A = dic_arr[i[0]]
        A.append(i[1])
        dic_arr[i[0]] = A
    
    stack = [(1,0,[0])] # 양의수, 늑대의수, 현재 위치
    max_cnt = 0
    print(dic_arr)
    while stack:
        print(stack)
        sheep_cnt, wolf_cnt, visited = stack.pop() # 1 0 0
        max_cnt = max(max_cnt, sheep_cnt)
        for i in visited: # 0
            for j in dic_arr[i]:  # 1 8
                if j not in visited:
                    current_sheep = sheep_cnt # 1
                    current_wolf = wolf_cnt # 0
                    if info[j] == 0: # 양일 경우
                        current_sheep += 1
                    else: # 늑대일 경우
                        current_wolf += 1
                    if current_wolf >= current_sheep:
                        continue
                    
                    stack.append((current_sheep, current_wolf, visited + [j]))
            # 2 0 1
    
    return max_cnt