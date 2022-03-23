# 못생긴수

N = int(input())


idx2, idx3, idx5 = 0,0,0
second, third, fifth = 2,3,5

ugly = [0] * N
ugly[0] = 1


for i in range(1, N):
    print(second, third, fifth)
    print(ugly)
    print(' ')
    ugly[i] = min(second, third, fifth) # 6 6 5
    
    if ugly[i] == second:
        idx2 += 1
        second = ugly[idx2] * 2
    if ugly[i] == third:
        idx3 += 1
        third = ugly[idx3] * 3
    if ugly[i] == fifth:
        idx5 += 1
        fifth = ugly[idx5] * 5

print(ugly)
    