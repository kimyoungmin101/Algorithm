from collections import deque

def solution(board):
    answer = 0
    board_map = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                board[i][j] = 101
            else:
                board[i][j] = 1000
                
    start_idx = deque([[[0,0], [0,1]]])
    board[0][0] = 0
    board[0][1] = 0
    
    cnt = 0
    while start_idx:
        first, second = start_idx.popleft()
        cnt += 1
        dx = second[0]
        dy = second[1]
        
        if first[0] == second[0]: # X 값이 같은경우 ㅡ
            if second[1] + 1 < len(board):
                if board[second[0]][second[1]+1] != 101:
                    start_idx.append([[dx,dy],[dx,dy+1]])
                    A = board[second[0]][second[1]+1]
                    B = board[second[0]][second[1]] + 1
                    board[second[0]][second[1]+1] = min(A, B)

            # 시계 방향으로 회전할 수 있는 경우
            if first[0] + 1 < len(board):
                if board[first[0]+1][first[1]] != 101 and board[second[0]+1][second[1]] != 101:
                    dx_f = first[0]
                    dy_f = first[1]
                    start_idx.append([[dx_f, dy_f],[dx_f + 1, dy_f]])

                    A = board[first[0]+1][first[1]]
                    B = board[second[0]+1][second[1]+1] + 1
                    board[first[0]+1][first[1]] = min(A, B)

            # 반시계 방향으로 회전할 수 있는 경우
            if second[0] + 1 < len(board):
                if board[first[0]+1][first[1]] != 101 and board[second[0]+1][second[1]] != 101:
                    start_idx.append([[dx, dy], [dx+1, dy]])
                    A = board[second[0]+1][second[1]]
                    B = board[second[0]][second[1]] + 1
                    board[second[0]+1][second[1]] = min(A, B)

        # ㅣ 이렇게 있을 때
        # 반시계 반향으로 회전할 수 있는 경우
        if first[1] == second[1]: # Y값이 같은경우 ㅣ 이런경우
            # 반시계 방향으로
            if first[1] -1 >= 0:
                if board[first[0]][first[1]-1] != 101 and board[second[0]][second[1]-1] != 101:
                    start_idx.append([[[first[0], first[1] - 1]], [first[0], first[1]]])
                    A = board[first[0]][first[1]-1]
                    B = board[second[0]][second[1]] + 1
                    board[first[0]][first[1]-1] = min(A, B)

            # 시계 방향으로 회전할 수 있는 경우
            if second[1] + 1 < len(board):
                if board[first[0]][first[1]+1] != 101 and board[second[0]][second[1]+1] != 101:
                    start_idx.append([[dx, dy], [dx, dy+1]])
                    A = board[second[0]][second[1]+1]
                    B = board[second[0]][second[1]] + 1
                    board[second[0]][second[1]+1] = min(A, B)

            # 아래로 갈 수 있는 경우
            if second[0] + 1 < len(board):
                if board[second[0]+1][second[1]] != 101:
                    start_idx.append([[dx,dy],[dx+1, dy]])

                    A = board[second[0]+1][second[1]]
                    B = board[second[0]][second[1]] + 1
                    board[second[0]+1][second[1]] = min(A, B)
        
    for i in board:
        print(i)
    '''
    아래로 가기위해서는 자리 차지 하고 있는 두칸 모두 [x+1][y]가 0이어야 한다
    '''
    
    return board[-1][-1]

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])