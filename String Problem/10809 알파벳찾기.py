alpha = [-1] * 26

S = input()

for i in range(len(S)):
    A = S[i] # b
    if(alpha[ord(A) - 97] == -1):
        alpha[ord(A) - 97] = i


for i in range(len(alpha)):
    print(alpha[i], end =' ')
