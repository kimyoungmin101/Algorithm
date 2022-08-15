# https://www.acmicpc.net/problem/17143

R, C, M = map(int, input().split())

dx = [-1,1,0,0] # 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
dy = [0,0,1,-1]

board = [[[] for _ in range(C+1)] for _ in range(R+1)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = [r, c, s, d, z]


fish_king = [0,0] # 현재 위치
cnt = 0


for i in range(C):
    # 1)낚시왕이 오른쪽으로 한 칸 이동한다.
    fish_king[1] += 1
    f_Y = fish_king[1] # 낚시왕이 있는 열
    
    # 2)낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for j in range(1, R+1):
        if board[j][f_Y] != []:
            cnt += board[j][f_Y][4] # 잡힌 상어 크기를 더함
            board[j][f_Y] = []
            break
    
    # 3)상어가 이동한다.
    new_board = [[[] for _ in range(C+1)] for _ in range(R+1)]
    
    for j in range(1, len(board)):
        for k in range(1, len(board[j])):
            if board[j][k] != []:
                r, c, s, d, z = board[j][k] # s : 속력 , d : 방향, z : 크기
                # 방향 d
                origin_s = s
                d_X = dx[d-1]
                d_Y = dy[d-1]
                
                if d == 3 or d == 4:
                    if d == 3: # 오른쪽인 경우
                        s += (c-1)
                        c = 1
                    elif d == 4: # 왼쪽인 경우
                        s += ((C-1) + (C - c)) # 5 + 1
                        c = 1
                        d = 3
                    
                    m_s = s // (C-1) # 몫
                    d_s = s % (C-1) # 나머지
                
                    if m_s % 2 != 0: # 홀수인경우
                        d = 4 # 방향 반대로
                        c = (C-d_s)
                    else: # 짝수인경우
                        c += d_s
                    
                else:
                    if d == 2: # 아래인 경우
                        s += (r - 1)
                        r = 1
                    elif d== 1: # 위인경우
                        s += ((R-1) + (R - r)) # 3 + 0
                        r = 1
                        d = 2
                    
                    m_s = s // (R-1) # 몫
                    d_s = s % (R-1) # 나머지
                
                    if m_s % 2 != 0: # 홀수인경우
                        d = 1 # 방향 반대로
                        r = (R - d_s)
                    else: # 짝수인경우
                        r += d_s
                
                if new_board[r][c] != []: 
                    cnt_weight = new_board[r][c][4]
                    new_weight = z
                    if cnt_weight < new_weight:
                        new_board[r][c] = [r, c, origin_s, d, z]
                else:
                    new_board[r][c] = [r, c, origin_s, d, z]
    board = new_board.copy()
    

print(cnt)