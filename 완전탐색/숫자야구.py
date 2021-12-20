N = int(input())

# 1 2 3 / 1 3 2 / 3 2 1 / 2 1 3
# 3 2 1 / 0 5 0 / 0 0 6
# 3 2 1 / 3 2 6 /
# 1 1 1 ~ 9 9 9
ans = []
result = [False for _ in range(N)]

for i in range(N):
    ans.append(list(map(int, input().split())))

# 111 123 1 1
def play(num, target, strike, ball, count):
    st = 0
    ba = 0
    nu = str(num) # 132
    ta = str(target) # 123
    for i in range(len(nu)):
        if(nu[i] == ta[i]):
            st += 1
            continue
        elif(nu[i] != ta[i] and nu[i] in ta):
            ba += 1
            continue
    
    if st == strike and ba == ball :
        count += 1

    return count

results = []

for i in range(111, 1000):
    str_i = str(i)
    if('0' in str_i):
        continue
    if(str_i[0] == str_i[1] or str_i[1] == str_i[2] or str_i[0] == str_i[2]):
        continue
    count = 0
    for j in ans:
        count = play(i, j[0], j[1], j[2], count)
        if(count == 0):
            break
        if count == (len(ans)):
            results.append(i)

print(len(results))