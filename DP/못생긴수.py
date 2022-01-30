# 알고리즘 교재 381페이지

# 
from math import sqrt


N = int(input())

def find_sosu(num):
    if num == 1 or num == 2:
        return True
    for X in range(2, int(sqrt(num))+1):
        if num % X == 0:
            return False
    return True

DP = []

def find_bool(X):
    # 1 2 3 4 5 6 8 9
    # 소수인 수와 7로 나누어 떨어지는 수는 못생긴 수가 아니다,
    if X % 7 == 0:
        return False
    if X > 10 and find_sosu(X):
        return False

    return True

for i in range(1, 1001):
    result_bool = find_bool(i)
    if result_bool:
        DP.append(i)

print(DP[:100])