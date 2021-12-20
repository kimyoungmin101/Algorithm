import sys

n = int(sys.stdin.readline())
N = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))


hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1


for i in M:
    if(i not in hashmap):
        print(0, end= " ")
    else:
        print(hashmap[i], end = " ")
