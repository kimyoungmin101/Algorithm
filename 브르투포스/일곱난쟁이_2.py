arr = []

for i in range(9):
    arr.append(int(input()))

visited = [False for _ in range(9)]
ans = []

def recur(X):
    global ans
    if(visited.count(True) == 7):
        sum_result = 0
        for i in range(9):
            if visited[i] == True:
                sum_result += arr[i]
        if sum_result == 100:
            ans = visited.copy()
            return
        else:
            return

    for i in range(9):
        if(visited[i] == False):
            visited[i] = True
            recur(X+1)
            visited[i] = False
            

recur(1)
results = []

for i in range(len(ans)):
    if ans[i] == True:
        results.append(arr[i])

results.sort()

for i in results:
    print(i)
    


'''
20
7
23
19
10
15
25
8
13
'''