# 문자열 뒤집기

S = str(input())
new_S = ''
cnt = S[0]

for i in range(1, len(S)):
    if S[i] != cnt:
        new_S += cnt
        cnt = S[i]

new_S += cnt

zero_cnt = new_S.count('0')
one_cnt = new_S.count('1')

result = min(zero_cnt, one_cnt)

print(result)