for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    f = 1
    while(x <= M*N):
        if x % N == y % N: # 83 % 11 == 6 % 11 / 13 11 5 6
            print(x)
            f = 0
            break
        x += M
    if f:
        print(-1)

# 포인트 !! x에 M을 더해도 x이다 !! 
# 10*X + 3 = 12*Y + 9 / 10X = 12Y + 6