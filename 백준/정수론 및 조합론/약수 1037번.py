N = int(input())

listr = list(map(int, input().split()))

listr.sort()

print(listr[0] * listr[-1])
