N = int(input())
arr = list(map(int, input().split()))
arr.sort()

guild = []
visited_arr = []
ans = 0
for i in arr:
    visited_arr.append(i)
    if len(visited_arr) == i:
        ans += 1
        visited_arr = []

print(ans)

'''
2 3 1 2 2
'''