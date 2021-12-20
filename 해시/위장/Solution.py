def solution(clothes):
    answer = 0
    # clothes = sorted(clothes, key = lambda x : x[1])
    dic = {}
    list = []
    for i in clothes:
        if(i[1] in dic):
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1

    for i in dic.values():
        list.append(i)
    
    cnt = 1
    for i in list:
        cnt *= (i+1)
    return cnt - 1
