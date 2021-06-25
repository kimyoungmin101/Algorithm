arr = []

import sys 
from collections import Counter

N = int(sys.stdin.readline())


for i in range(N):
    A = int(sys.stdin.readline())
    arr.append(A)

arr.sort()
print(int(round(sum(arr)/len(arr),0)))
print(arr[len(arr)//2])

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

print(mode(arr))
print(max(arr) - min(arr))
