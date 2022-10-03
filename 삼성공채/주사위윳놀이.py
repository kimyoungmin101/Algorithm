# https://www.acmicpc.net/problem/17825

graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
dice = list(map(int, input().split()))
answer = 0


# index가 32 일때 마지막 도착이다.
def dfs(cnt_sum, cnt, value):
    global answer
    
    if cnt >= 10:
        answer = max(answer, cnt_sum)
        return

    for i in range(4):
        cnt_idx = value[i] # 현재의 인덱스
        
        if len(graph[cnt_idx]) >= 2: # 현재의 인덱스가 파란색 칸인 경우
            cnt_idx = graph[cnt_idx][1]
        else:
            cnt_idx = graph[cnt_idx][0]
        
        for j in range(1, dice[cnt]): # Dice만큼 이동 한다.
            cnt_idx = graph[cnt_idx][0]
            
        # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
        if cnt_idx == 32 or (cnt_idx < 32 and cnt_idx not in value):
            before = value[i]
            value[i] = cnt_idx
            dfs(cnt_sum + score[cnt_idx], cnt + 1, value)
            value[i] = before
            
dfs(0,0, [0,0,0,0])
print(answer)