T = int(input())


def facto(R):
    arr = [1, 1, 2, 6] # DP를 이용한 팩토그램!
    for i in range(4, R+1): # 팩토그램 정리
        arr.append(arr[i-1] * i)
    return arr

for i in range(T):
    R, N = map(int, input().split())
    arr = facto(N)
    A = arr[N] // (arr[R]*arr[N-R])
    print(A)
# nCr을 이용하여 풀자. 서로다른 N개의 조합중 r개를 선택할떄!
# n! / r!(n-r)!


