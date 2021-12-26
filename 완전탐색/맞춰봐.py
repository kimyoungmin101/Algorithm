N = int(input())
S_N = str(input())
S_result = [i for i in S_N]
real_N = N
arr_result = []

while S_result:
    arr_result.append(S_result[:N])
    S_result = S_result[N:]
    N -= 1
    
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
    if(X == M+1):
        for i in range(len(arr_result)):
            sum_result = 0
            for j in range(len(arr_result[i])):
                Q = i + j + 1
                sum_result += arr[Q]
                if arr_result[i][j] == '-':
                    if sum_result >= 0:
                        return
                elif arr_result[i][j] == '0':
                    if sum_result != 0:
                        return
                else:
                    if sum_result <= 0:
                        return
        if result_bool == False:
            result_arr = arr.copy()
            for i in range(1, len(result_arr)):
                print(result_arr[i], end = ' ')
            print('')
            result_bool = True
        return
        
    for i in range(-10, N+1):
        arr[X] = i
        recur(X+1)

recur(1)
