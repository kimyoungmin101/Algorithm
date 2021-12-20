N = int(input())

# 1 ~ 9 => 1 / 10 ~ 99 => 2 / 100 ~ 999 => 3 / 1000 ~ 9999 => 4

# 120

A = N
cnt = 0
# 120
if N < 10:
    print(N)
else:
    while A != 0:
        cnt += 1
        A = A // 10
        
    # cnt = 자리수 10 * 3
    Q = 10**(cnt - 1) # 100
    count = 0
    first = False
    
    while Q != 0:
        if first == False:
            count += ((N - Q + 1) * cnt) # 21 * 3
            first = True
            Q = (Q // 10) # 10
            cnt -= 1
        else:
            count += ((Q * 9) * cnt)
            cnt -= 1
            Q = (Q // 10)

    print(count)

# 63 + 180 + 9