N = int(input())

star = []
for _ in range(N):
    star.append(["*" for _ in range(N)])


    
divide = N
cnt = 0

while divide != 1:
    divide /= 3
    cnt += 1

for n in range(cnt):
    # 빈칸인 인덱스 구하기
    idx = [i for i in range(N) if (i // 3 ** n) % 3 == 1]
    for i in idx:
        for j in idx:
            star[i][j] = " "

# 프린트

for _ in star:
    print("".join(_))


# list에서 문자열로 가려면 join(리스트)
# 문자열에서 list로 가려면 split(기준)
