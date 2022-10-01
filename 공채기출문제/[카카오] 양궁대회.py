remember = []
answer = 0
set_new = []

def dfs(arr, cnt, info, n):
    global answer, remember
    
    if cnt == n:
        lion = 0
        apeach = 0
        
        for i in range(11):
            if info[i] == 0 and arr[i] == 0:
                continue
            if info[i] >= arr[i]:
                apeach += (10 - i)
            else:
                lion += (10 - i)
        
        if lion > apeach:
            if answer < (lion - apeach):
                answer = lion - apeach
                remember = arr.copy()

        return
    
    for i in range(11):
        arr[i] += 1
        dfs(arr, cnt + 1, info, n)
        arr[i] -= 1
        
def solution(n, info):
    arr = [0 for _ in range(11)]
        
    dfs(arr, 0, info, n)
    return remember

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

# 5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]