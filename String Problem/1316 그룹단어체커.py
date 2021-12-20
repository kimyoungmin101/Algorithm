N = int(input())

jlist = []
count = 0

for i in range(N):
    S = input()
    for j in range(len(S)):
        if(j == 0):
            jlist.append(S[j])
            continue
        elif(S[j] == S[j-1]):
            continue
        else:
            jlist.append(S[j])
    for j in range(len(jlist)):
        if(jlist.count(jlist[j]) >= 2):
            break
        if(j == (len(jlist) - 1)):
            count += 1
    jlist = []
                
print(count)
