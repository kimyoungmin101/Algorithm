N = int(input())
K = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(K):
    X, Y = map(int ,input().split())
    graph[X-1][Y-1] = 1

L = int(input())

arrow = []

for i in range(L):
    A , B = map(str, input().split())

    arrow.append([int(A), B])

tail = 0
cnt_arrow = 0 # 오른쪽 dx dy idx
cnt_graph = [0,0]
log = []

dx = [0,1,0,-1] # 오른쪽 아래, 왼쪽, 위쪽
dy = [1,0,-1,0]

time = 0
break_game = False
real_tail = [0,0]

def go_to(A, B):
    global cnt_arrow, time, break_game, tail

    X = dx[cnt_arrow] # 0
    Y = dy[cnt_arrow] # 1
    
    now_time = time
    while A - now_time:
        log.append([cnt_graph[0],cnt_graph[1]])

        cnt_graph[0] += X
        cnt_graph[1] += Y

        if [cnt_graph[0], cnt_graph[1]] in log:
            break_game = True
            return time

        if cnt_graph[0] >= N or cnt_graph[1] >= N or cnt_graph[0] < 0 or cnt_graph[1] < 0:
            break_game = True
            return time
        
        if graph[cnt_graph[0]][cnt_graph[1]] == 1:
            graph[cnt_graph[0]][cnt_graph[1]] = 0
            tail += 1
        
        if len(log) > tail:
            log.pop(0)
        
        time += 1
        
        A -= 1

    if B == 'D':
        cnt_arrow = (cnt_arrow + 1) % 4
    elif B == 'L':
        if (cnt_arrow - 1) < 0:
            cnt_arrow = 3
        else:
            cnt_arrow -= 1

    return time

while arrow:
    A = arrow.pop(0) # [8, 'D']
    
    time = go_to(A[0], A[1])

    if break_game:
        break

if break_game == False:
    time = go_to(N + 1,'D')

print(time + 1)
