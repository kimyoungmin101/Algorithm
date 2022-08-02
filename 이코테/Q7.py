# 럭키 스트레이트

# 럭키스트레이트 https://www.acmicpc.net/problem/18406

N = str(input())

'''
123402
'''

N_left = N[:len(N)//2]
N_right = N[len(N)//2:]

N_left = list(map(int, N_left.strip()))
N_right = list(map(int, N_right.strip()))

left_sum = sum(N_left)
right_sum = sum(N_right)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")