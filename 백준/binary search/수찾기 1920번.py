from sys import stdin, stdout

n = stdin.readline()
N = sorted(stdin.readline().split())

m = stdin.readline()
M = stdin.readline().split()

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)
        

for i in range(len(M)):
    start = 0
    end = len(N) - 1
    print(binary(M[i], N, start, end))
