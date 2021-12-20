S = input()
count = 0
Z = S
    
crlist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in crlist:
    while(i in S):
        A = S.index(i)
        S = S[:A] + '*' + S[len(i)+A:]
        count += 1

for i in S:
    if(i != '*'):
        count += 1
    else:
        continue

print(count)
