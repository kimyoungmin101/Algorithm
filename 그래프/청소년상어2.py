import copy
import heapq

fish_arr = [] # 물고기가 담긴 리스트
arrow_arr = [] # 방향이 담긴 리스트
cnt_shark = [0,0]

arrow_str = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']

for i in range(4):
    fish = []
    arrow = []
    A = list(map(int, input().split()))
    for j in range(len(A)):
        if j % 2 == 0: # 짝수이면   
            fish.append(A[j])
        else: # 홀수이면
            arrow.append(A[j])
    fish_arr.append(fish)
    arrow_arr.append(arrow)

