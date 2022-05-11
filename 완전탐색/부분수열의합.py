# https://www.acmicpc.net/problem/1182

N, S = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
ans = []

def recursive(A, result):
    global S, cnt
    
    if result == S and len(ans) != 0:
        cnt += 1

    for i in range(A, len(arr)):
        if i in ans:
            continue
        if len(ans) >= 1:
            if ans[-1] > i:
                continue
        ans.append(i)
        result += arr[i]
        recursive(A+1, result)
        result -= arr[i]
        ans.pop()
        
recursive(0, 0)

print(cnt)