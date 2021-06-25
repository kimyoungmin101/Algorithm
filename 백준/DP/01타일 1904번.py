N = int(input())

def dp(N):
    arr = [0, 1, 2]
    for i in range(3, N + 1):
        arr.append((arr[i-2] + arr[i-1]) % 15746)
    return arr[N] 
print(dp(N))
