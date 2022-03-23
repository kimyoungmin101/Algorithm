# 편집 거리

str_first = str(input())
str_second = str(input())

str_first = list(str_first.strip())
str_second = list(str_second.strip())


'''
sunday
saturday
'''

long_str = []
short_str = []

if len(str_first) >= len(str_second):
    long_str = str_first.copy()
    short_str = str_second.copy()
else:
    long_str = str_second.copy()
    short_str = str_first.copy()

DP = [[0 for _ in range(len(long_str) + 1)] for _ in range(len(short_str) + 1)]

for i in range(len(DP)):
    DP[i][0] = i
for i in range(len(DP[0])):
    DP[0][i] = i

for i in range(1, len(DP)):
    for j in range(1, len(DP[0])):
        if short_str[i-1] == long_str[j-1]:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = 1 + min(DP[i][j-1], DP[i-1][j-1], DP[i-1][j])

for i in DP:
    print(i)


