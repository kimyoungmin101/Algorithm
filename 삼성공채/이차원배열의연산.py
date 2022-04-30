# https://www.acmicpc.net/problem/17140


r,c,k = map(int, input().split())

cnt = 0

arr = []

for i in range(3):
    arr.append(list(map(int, input().split())))
    
def solution(newArr): # R연산
    maxLen = 0
    nxtArr = []
    
    for i in range(len(newArr)):
        home = [[_, 102] for _ in range(102)]

        value = newArr[i]
        
        for j in value:
            if j == 0:
                continue
            
            if home[j][1] == 102:
                home[j][1] = 1
            else:
                home[j][1] += 1
                
        home = sorted(home, key = lambda X : (X[1], X[0]))
        
        newValue = []
        
        for j in home:
            if j[1] == 102:
                break
            newValue.append(j[0])
            newValue.append(j[1])
        
        if len(newValue) > 100:
            newValue = newValue[:100]
        
        nxtArr.append(newValue)
        
        maxLen = max(maxLen, len(newValue))
            
    for i in range(len(nxtArr)):
        len_num = len(nxtArr[i]) # 4
        for j in range(maxLen-len_num): # 2
            nxtArr[i].append(0)
    
    return nxtArr

def rotate(newArr):
    newArr = list(zip(*newArr[::1]))
    return newArr

while cnt <= 101:
    
    if len(arr) >= r and len(arr[0]) >= c:
        if arr[r-1][c-1] == k:
            break
    
    if len(arr) >= len(arr[0]): # 행의개수 >= 열의개수 R연산
        arr = solution(arr)
    else: # 열의개수 > 행의개수 C연산
        arr = rotate(arr)
        arr = solution(arr)
        arr = rotate(arr)
    
    cnt += 1
    
if cnt > 100:
    print(-1)
else:
    print(cnt)
    