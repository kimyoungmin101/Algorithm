N, K = map(int, input().split())

arr = [1, 1, 2, 6] # DP를 이용한 팩토그램!

for i in range(4, N+1): # 팩토그램 정리
    arr.append(arr[i-1] * i)

A = arr[N]//(arr[K]*arr[N-K]) # 이항정리 공식

print(A % 10007)
