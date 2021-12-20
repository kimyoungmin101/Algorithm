from itertools import combinations

N = int(input())
arr = [x for x in range(N)]
cases = list(combinations(arr, int(N/2)))
for i in range(N):
	arr[i] = list(map(int, input().split()))

min_value = 100*N*N

for case_a in cases:
	stat_A = 0
	stat_B = 0

	for x in case_a:
		for y in case_a:
			stat_A += arr[x][y]
	case_b = [x for x in range(N) if x not in case_a]

	for x in case_b:
		for y in case_b:
			stat_B += arr[x][y]
	min_value = min(min_value, abs(stat_A-stat_B))
    

print(min_value)
