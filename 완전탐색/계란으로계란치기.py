# https://www.acmicpc.net/problem/16987
import copy

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

max_cnt = 0

def recursive(start, cnt_arr):
    global N, max_cnt
        
    if start == len(arr):
        b_cnt = 0
        for k in cnt_arr:
            if k[0] <= 0:
                b_cnt += 1
            
        max_cnt = max(b_cnt, max_cnt)
        
        return
    
    if cnt_arr[start][0] <= 0:
        recursive(start + 1, cnt_arr)
    else:
        flag = False
        for i in range(N):
            if i == start or cnt_arr[i][0] <= 0:
                continue
            else:                
                cnt_arr[start][0] -= cnt_arr[i][1]
                cnt_arr[i][0] -= cnt_arr[start][1]
                
                flag = True
                recursive(start + 1, cnt_arr)

                cnt_arr[start][0] += cnt_arr[i][1]
                cnt_arr[i][0] += cnt_arr[start][1]
        if not flag:
            recursive(start + 1, cnt_arr)
            
recursive(0, arr[:])

print(max_cnt)