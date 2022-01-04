S = list(map(str, str(input().strip())))

S.sort()
start_idx = 0
for i in range(len(S)):
    try:
        A = int(S[i])
    except:
        start_idx = i
        break

int_S = S[:start_idx]
str_S = S[start_idx:]

int_S = list(map(int, int_S))
str_S = list(map(str, str_S))

str_S.append(str(sum(int_S)))
result = ''.join(str_S)

print(result)


'''
K1KA5CB7

AJKDLSI412K4JSJ9D
'''