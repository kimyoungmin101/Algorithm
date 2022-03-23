# 정수 삼각형 https://www.acmicpc.net/problem/1932

N = int(input())

triangle = []
ans = []
for i in range(N):
    arr = list(map(int, input().split()))
    triangle.append(arr)
    ans.append([0 for _ in range(len(arr))])
    
ans[0][0] = triangle[0][0]

for i in range(len(triangle) - 1):
    for j in range(len(triangle[i])):
        ans[i+1][j] = max(ans[i+1][j], triangle[i+1][j] + ans[i][j])
        ans[i+1][j+1] = max(ans[i+1][j+1], triangle[i+1][j+1] + ans[i][j])

max_result = max(ans[-1])
print(max_result)
            
