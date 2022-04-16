def solution(info, edges):
    answer = 0
    dic_arr = {}

    for i in range(len(info)):
        dic_arr[i] = []

    for i in edges:
        A = dic_arr[i[0]]
        A.append(i[1])
        dic_arr[i[0]] = A

    stack = [(1,0,[0])] # 양의수, 늑대의수, 현재 위치
    max_cnt = 0
    
    while stack:
        sheep_cnt, wolf_cnt, visited = stack.pop() # 1 0 0
        
        max_cnt = max(max_cnt, sheep_cnt)
        for i in visited:
            for j in dic_arr[i]:
                if j not in visited:
                    if info[j] == 0: # 양이면
                        nxt_sheep = sheep_cnt + 1
                        nxt_wolf = wolf_cnt
                        newVisited = visited[:]
                        newVisited.append(j)
                        stack.append((nxt_sheep, nxt_wolf, newVisited))
                    else: # 늑대이면
                        nxt_sheep = sheep_cnt
                        nxt_wolf = wolf_cnt + 1
                        if nxt_sheep > nxt_wolf:
                            newVisited = visited[:]
                            newVisited.append(j)
                            stack.append((nxt_sheep, nxt_wolf, newVisited))
    
    return max_cnt

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))