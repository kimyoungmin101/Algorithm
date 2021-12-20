N = int(input())

def facto(R):
    arr = [1, 1, 2, 6] # DP를 이용한 팩토그램!
    for i in range(4, R+1): # 팩토그램 정리
        arr.append(arr[i-1] * i)
    return arr[R]

A = (str(facto(N)))
    
ans = ''

for i in range(len(A)-1, -1, -1):
    ans += A[i]

result = 0

for i in ans:
    if(i == '0'):
        result += 1
    else:
        break

print(result)
    
