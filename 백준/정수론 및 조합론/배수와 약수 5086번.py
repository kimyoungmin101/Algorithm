while(True):
    N, M = map(int, input().split())
    if(N == 0 and M == 0):
        break
    elif(N > M and N % M == 0):
        print('multiple')
        continue
    elif(N < M and M % N == 0):
        print('factor')
        continue
    else:
        print('neither')
        continue
