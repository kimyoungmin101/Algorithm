arr = list(map(int, input().split()))

E = arr[0] # 1 ≤ E ≤ 15
S = arr[1] # 1 ≤ S ≤ 28
M = arr[2] # 1 ≤ M ≤ 19



def solution(E,S,M):
    count = 0
    X, Y, Z = 0, 0, 0

    while(True):
        count += 1
        if( count % 15 == 0 ):
            X = 15
        else:
            X = count % 15

        if count % 28 == 0:
            Y = 28
        else:
            Y = count % 28

        if count % 19 == 0:
            Z = 19
        else:
            Z = count % 19
        
        if(X == E and Y == S and M == Z):
            return count

print(solution(E,S,M))