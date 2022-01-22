# 백준 https://www.acmicpc.net/problem/1715
import heapq

N = int(input())
heapq_arr = []

for i in range(N):
    heapq.heappush(heapq_arr, int(input()))
answer = 0
while len(heapq_arr) > 1:
    A = heapq.heappop(heapq_arr) # 제일 작은 수
    B = heapq.heappop(heapq_arr) # 두번째로 작은 수
    answer += (A + B)
    heapq.heappush(heapq_arr, A + B)

print(answer)

# (10 + 20) + (30 + 30) + (40 + 50) + (60 + 90)
# 30 + 60 + 90 + 150 = 330