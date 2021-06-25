N = int(input())

arrN = list(map(int, input().split()))
arrP = list(map(int, input().split()))

arrP = arrP[:-1]
ans = 0
minn = 1000000000

while(arrN):
    A = arrN.pop(0)
    B = arrP.pop(0)
    if(B < minn):
        minn = B
    ans += (minn * A)

print(ans)
    
