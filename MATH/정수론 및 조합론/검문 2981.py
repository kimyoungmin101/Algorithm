def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))

min_n = min(ls) #최솟값 구하기

for i in range(len(ls)):
    if ls[i] > min_n:
        ls[i] = ls[i] - min_n
        #모든 자연수를 최솟값으로 빼주기

ls.remove(min_n)
        #최솟값은 원래 리스트에서 제거

#위에서 계산한 자연수-최솟값들 모두의 최대 공약수 구하기
gcd_n = ls[0]
for i in range(len(ls)):
    gcd_n = gcd(gcd_n, ls[i])
    #최대 공약수의 약수 구하기

for i in range(2, gcd_n+1):
    if gcd_n%i==0:
        print(i,end = ' ')
