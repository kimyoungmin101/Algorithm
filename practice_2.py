solution_arr = []

def get_result(start, N, arr, visited):
    if len(arr) == 1:
        solution_arr.append(arr.copy())
    else:
        is_ans = True
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                is_ans = False
                break
        if is_ans:
            solution_arr.append(arr.copy())
    
    if len(arr) == 1:
        if arr[0] == N:
            return
    
    for i in range(N+1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            get_result(start+1, N, arr, visited)
            arr.pop()
            visited[i] = False
    
    
    
def solution(height, width):
    new_ans = []
    for i in range(len(height)):
        new_ans.append([height[i], width[i]])
    
    N = len(height)
    visited = [False for _ in range(N)]
    
    get_result(0, N-1, [], visited)
    
    
    ans = 0
    
    for i in range(1, len(solution_arr)):
        min_Y = 400001
        max_X = 0
        max_result = 0
        for j in solution_arr[i]:
            max_result = max(height[j] * width[j], max_result)
        
        for j in solution_arr[i]:
            min_Y = min(min_Y, height[j])
            max_X += width[j]
        
        max_result = max(max_X * min_Y, max_result)
        ans = max(max_result, ans)
    
    return ans


print(solution([140, 21, 21, 32], [2, 1, 3, 7]))