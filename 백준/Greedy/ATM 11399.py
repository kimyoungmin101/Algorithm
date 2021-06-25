N = int(input())
A = list(map(int, input().split()))

# 먼저 정렬을한다.
# 3 1 4 3 2
A.sort()
# 1 2 3 3 4
ans = 0 # 누적합
realans = 0


for i in A:
    ans += i # A는 각 사람들이 돈뽑은 시간
    realans += ans # 최종으로 돈을 다 뽑아내는 최소시간

print(realans)

