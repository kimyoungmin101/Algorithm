N = input()

N = int(N)
count = 0

list = [0, 0]
list[0] = 1
list[1] = 6
answer = [0, 0]
answer[0] = 1
answer[1] = 7

i = 2

while(answer[i-1] <= 10000):
    list.append( list[i-1] + 6 )
    answer.append( answer[i-1] + list[i] )
    if(N <= answer[i] and N >= 19):
        print(i + 1)
        break
    else:
        if( N == 1):
            print(1)
            break
        elif( N <= 7):
            print(2)
            break
        elif( N <= 19):
            print(3)
            break
        else:
            i += 1
