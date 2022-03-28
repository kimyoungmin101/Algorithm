'''
5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1
'''
answer_count = 0

def rotate(arr):
    ans = []
    
    for i in range(4):
        
        arr = list(zip(*arr[::-1]))
        
        for j in range(len(arr)):
            arr[j] = list(arr[j])
        
        if arr not in ans:
            ans.append(arr)
        
    return ans

def result(ans, tatelo):
    # [True], [True], [True], [True]]
    global answer_count
    
    X_len = len(tatelo) # 4
    Y_len = len(tatelo[0]) # 1
    
    if len(ans) < X_len or len(ans) < Y_len:
        return
    
    for i in range(len(ans) - X_len + 1):
        for j in range(len(ans[0]) - Y_len + 1):
            Z = 0
            for k in range(len(tatelo)):
                for q in range(len(tatelo[k])):
                    if tatelo[k][q] == True:
                        X = i + k
                        Y = j + q
                        Z += ans[X][Y]
            
            answer_count = max(answer_count, Z)

N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

one = [[True, True, True, True]]
two = [[True, True], [True, True]]
three = [[True, False],[True, False], [True,True]]
four = [[True,False],[True,True],[False, True]]
five = [[True, True, True] , [False, True, False]]
six = [[False,True],[False,True],[True,True]]
seven = [[False,True],[True,True],[True,False]]

one = rotate(one)
two = rotate(two)
three = rotate(three)
four = rotate(four)
five = rotate(five)
six = rotate(six)
seven = rotate(seven)

solution = [one, two, three, four, five, six, seven]

cnt = 0
for i in solution:
    for j in i:
        cnt += 1
        result(arr, j)

print(answer_count)