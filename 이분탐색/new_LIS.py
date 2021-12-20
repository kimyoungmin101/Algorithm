N = int(input())
array = list(map(int, input().split()))

# arr : 10 20 40 25 20 50 30 70 85
# 정답 : 10 20 40 50 70 85 / 길이 6
# 10
# 10 20
# 10 20 40 
# 10 20 25
# 10 20 25 50
# 10 20 25 30

from bisect import bisect_left

def binary_search(L, target):
    start = 0
    end = len(L)

    while start < end:
        mid = (start + end) // 2 # 2를 return 해야함 / # start : 2, mid : 2, end : 2

        if L[mid] < target:
            start = mid + 1 
        elif L[mid] == target:
            return mid
        else:
            end = mid

    return end


add_idx = [0]

def get_lis_improved(sequence):
  L = [sequence[0]]
  for i in range(1, len(sequence)):
    if L[-1] < sequence[i]:
      L.append(sequence[i])
      add_idx.append(len(L)-1)
    else:
      lower_bound = binary_search(L, sequence[i])
      add_idx.append(lower_bound)
      L[lower_bound] = sequence[i]
  # print(L)
  
  return L

result = get_lis_improved(array)

res = []
max_idx = max(add_idx)
while(max_idx >= 0):
    A = add_idx.pop()
    B = array.pop() 
    if A == max_idx:
        res.append(B)
        max_idx -= 1

print(len(result))
print(*reversed(res))
'''
9
3 1 2 4 7 5 6 8 10
'''