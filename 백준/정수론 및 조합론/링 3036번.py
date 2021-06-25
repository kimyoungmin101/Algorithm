N = int(input())

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a # 최대공약수

arr = list(map(int, input().split()))

ans = arr.pop(0)

for i in arr:
    A = gcd(ans, i) # ㅁ첫번째 수와 arr리스트 값들의 최대공약수를 구함
    print(str(ans//A) + "/" + str(i//A))
