T = int(input())

for i in range(T):
    ans = ''
    R, S = map(str, input().split())
    R = int(R)
    for i in range(len(S)):
        ans += (S[i] * R)
    print(ans)
