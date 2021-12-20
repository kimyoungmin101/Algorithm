N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            results = cards[i] + cards[j] + cards[k]
            if(results <= M and results > max_result):
                max_result = results


print(max_result)