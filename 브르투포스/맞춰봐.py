#부호와 합이 일치하는지 확인하는 함수
def ck(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and S[i][idx] != 0:
            return False
        elif hap < 0 and S[i][idx] >= 0:
            return False
        elif hap > 0 and S[i][idx] <= 0:
            return False
    return True

def solve(idx):
    if idx == N:
        return True
    if S[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i
        if ck(idx) and solve(idx+1):
            return True
    return False

N = int(input())
arr = list(input())
S = [[0]*N for i in range(N)]
print(arr)

for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N

solve(0)
print(' '.join(map(str, result)))

"""N = int(input())
arr_result = list(map(str, input().strip()))
real_N = N
    
N = real_N
M = N

arr = [0 for _ in range(real_N)]
visited = [False for _ in range(real_N)]

arr = [0] * (M + 1) # 2
N = 10
result = []
result_bool = False

def recur(X):
    global result_bool
    global real_N
    
    if(X == M+1):
        arr_copy = arr.copy()[1:]
        Q = real_N - 1  
        Z = real_N
        # 0 3 5 6
        arr_idx = [0 for _ in range(real_N)]
        arr_nxt = [0 for _ in range(real_N)]

        for i in range(1, len(arr_idx)):
            arr_idx[i] = arr_idx[i-1] + Q
            arr_nxt[i] = arr_nxt[i-1] + Z
            Q -= 1
            Z -= 1
        # arr_idx = [0 3 5 6]
        # arr_nxt = [0 4 7 9]
        # 0 1 2 3 / 1 2 3 / 2 3 / 3
        # 0 1 2 3 / 4 5 6 / 7 8 / 9
        result_sum = 0
        idx = 0
        for i in range(len(arr_result)):
            
            if i == arr_nxt[idx+1]:
                idx += 1
                result_sum = 0

            result_sum += arr_copy[i - arr_idx[idx]]

            if arr_result[i] == '-':
                if result_sum >= 0:
                    return
            elif arr_result[i] == '0':
                if result_sum != 0:
                    return
            else:
                if result_sum <= 0:
                    return

        if result_bool == False:
            for i in range(len(arr_copy)):
                print(arr_copy[i], end = ' ')
            print('')
            result_bool = True
        return
        
    for i in range(-10, N+1):
        arr[X] = i
        recur(X+1)

recur(1)"""
