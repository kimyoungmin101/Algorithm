N, M = map(int, input().split())

arr = []

for i in range(N):
    A = input()
    arrb = []
    for j in range(len(A)):
        arrb.append(A[j])
    arr.append(arrb)

q = []

def long(arrb, X, Y):
    count = 0
    for i in range(len(arrb)):
        for j in range(len(arrb[i])):
            if(i % 2 == 0 and j % 2 == 0):
                if(arrb[i][j] == X):
                    continue
                else:
                    count += 1
            elif(i % 2 == 0 and j % 2 != 0):
                if(arrb[i][j] == Y):
                    continue
                else:
                    count += 1
            elif(i % 2 != 0 and j % 2 == 0):
                if(arrb[i][j] == Y):
                    continue
                else:
                    count += 1
            else:
                if(arrb[i][j] == X):
                    continue
                else:
                    count += 1
    q.append(count)


def printt(arr):
    for i in range(N - 7):
        for j in range(M - 7):
            barr = [row[j:j+8] for row in arr[i:i+8]]
            long(barr, 'B', 'W')
            long(barr, 'W', 'B')
    print(min(q))


printt(arr)
