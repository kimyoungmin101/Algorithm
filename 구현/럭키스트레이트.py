# 백준 18406번

N = str(input())

half_N = len(N) // 2
N_first = N[:half_N]
N_second = N[half_N:]

N_first = list(map(int, N_first.strip()))
N_second = list(map(int, N_second.strip()))

first_sum = sum(N_first)
second_sum = sum(N_second)

if first_sum == second_sum:
    print('LUCKY')
else:
    print('READY')