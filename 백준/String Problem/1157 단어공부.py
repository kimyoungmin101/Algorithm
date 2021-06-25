S = input()

listS = [0] * 26

for i in range(len(S)):
    Q = S[i]
    Q = int(ord(Q))
    if(Q >= 97):
        Q -= 97
    else:
        Q -= 65
    listS[Q] += 1

ans = max(listS)
count = listS.count(ans)

if(count > 1):
    print('?')
else:
    print(chr(listS.index(ans)+65))

