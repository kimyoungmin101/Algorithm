INF = 9999999

def floyd(arr, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(arr[i][j] > arr[i][k] + arr[k][j]):
                    arr[i][j] = arr[i][k] + arr[k][j]

def solution(n, s, a, b, fares):
    answer = 0

    arr = [[INF for _ in range(n)] for _ in range(n)]

    for i in fares:
        arr[i[0]-1][i[1]-1] = i[2]
        arr[i[1]-1][i[0]-1] = i[2]

    for i in range(len(arr)):
        arr[i][i] = 0

    floyd(arr, n)
        
    answer = INF

    s -= 1
    a -= 1
    b -= 1


    for i in range(n):
        answer = min(answer, arr[s][i] + arr[i][b] + arr[i][a])    



    return answer