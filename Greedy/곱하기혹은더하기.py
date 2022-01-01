'''
P313번 그리디 문제
02984

567
'''

N = list(map(str, input().strip()))
N.sort()
result = 0

while(N):
    A = int(N.pop(0)) #0
    if A == 0:
        continue
    
    if result == 0 and A != 0:
        result += A
        continue

    if result * A > result + A:
        result = result * A
    else:
        result = result + A
    


print(result)