N = int(input())
budget = list(map(int, input().split()))
M = int(input())
budget.sort()

start, end = 0, budget[-1]
total_budget = 0

while start <= end:
    mid = (start+end) // 2

    total_budget = 0
    for i in budget:
        total_budget += min(mid, i)

    if total_budget > M:
        end = mid - 1
    else:
        start = mid + 1
print(end)