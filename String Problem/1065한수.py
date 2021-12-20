def hansu(n):
    if ( n < 100):
        return n
    else:
        ans = 99
        for i in range(100, n+1):
            q = i
            a = i
            num = 0
            while ( q > 0):
                q /= 10
                q = int(q)
                num += 1
                
            a = str(a) # 135
            re = 0
            for j in range(num):
                if(j == 0):
                    re = int(a[j + 1]) - int(a[j])
                elif( (j + 1) < num ):
                    if( re != (int(a[j + 1]) - int(a[j]))):
                        break
                if((j+1) == num):
                    ans += 1
    return ans

N = int(input())

print(hansu(N))
