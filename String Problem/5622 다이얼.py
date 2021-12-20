S = input()


dial = 0

for i in range(len(S)):
    if(S[i] == 'A' or S[i] == 'B' or S[i] == 'C'):
        dial += 3
    elif(S[i] == 'D' or S[i] == 'E' or S[i] == 'F'):
        dial += 4
    elif(S[i] == 'G' or S[i] == 'H' or S[i] == 'I'):
        dial += 5
    elif(S[i] == 'J' or S[i] == 'K' or S[i] == 'L'):
        dial += 6
    elif(S[i] == 'M' or S[i] == 'N' or S[i] == 'O'):
        dial += 7
    elif(S[i] == 'P' or S[i] == 'Q' or S[i] == 'R' or S[i] == 'S'):
        dial += 8
    elif(S[i] == 'T' or S[i] == 'U' or S[i] == 'V'):
        dial += 9
    else:
        dial += 10

print(dial)
