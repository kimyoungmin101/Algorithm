# https://www.acmicpc.net/problem/20055

from collections import deque
from logging import root

N, K = map(int, input().split())
arr = deque(list(map(int, input().split())))


# ㄴㅐ리는 위위치
down = N

# 올리는 위치 : 0
up = 0

# 로봇위치
robot = deque([])

# 벨트길이
belt_len = len(arr)

count = 1

while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    arr.rotate()
    
    for idx, value in enumerate(robot):
        robot[idx] += 1
        
    if N-1 in robot:
        robot.remove(N-1)
        
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for idx, value in enumerate(robot):
        next = (value + 1)
        if arr[next] >= 1 and next not in robot:
            arr[next] -= 1
            robot[idx] = next
            
    if N-1 in robot:
        robot.remove(N-1)
        
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if arr[up] > 0 and 0 not in robot:
        arr[up] -= 1
        robot.append(0)

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if arr.count(0) >= K:
        break
    else:
        count += 1

print(count)
