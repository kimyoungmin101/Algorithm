N = int(input())
import sys
arr = list(map(int, input().split()))
arr.sort()

print(arr[(len(arr)-1) // 2])
