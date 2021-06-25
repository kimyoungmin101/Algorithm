import math

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r_sum = r1+r2

    # A, B의 좌표가 같은 경우
    # 반지름이 같으면 -1, 반지름이 다르면 0
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    # A, B의 좌표가 다른 경우
    else:
        # A, B의 거리가 두 반지름의 합보다 크면 접점이 없다 0
        if dis > r_sum:
            print(0)
        # A, B의 거리가 두 반지름의 합과 같으면 한 점에서 만난다 1
        elif dis == r_sum:
            print(1)

        # A, B의 거리가 두 반지름의 합보다 작은 경우
        # 한 원 안에서 접하는 경우 1
        # 원 안에 들어가서 접점이 없는 경우 0
        # 이외의 경우에는 두 점에서 만남 2
        elif dis < r_sum:
            if (dis+min(r1,r2)) == max(r1,r2):
                print(1)
            elif(dis+min(r1,r2)) < max(r1,r2):
                print(0)
            else:
                print(2)

