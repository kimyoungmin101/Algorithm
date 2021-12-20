# 5개 /
N, K = map(int, input().split())
str_arr = []

learn_str = ['a', 'n', 't', 'i', 'c']
notyet_learn = []

for i in range(N):
    A = str(input())
    A = A[4:]
    A = A[:-4]
    real_str = ''
    for i in A:
        if i not in learn_str:
            real_str += i
            if i not in notyet_learn:
                notyet_learn.append(i)

    str_arr.append(real_str)


if K < 5:
    print('0')
else:
    can_learn = K - 5
    checked = [False for _ in range(len(notyet_learn))]
    arr_i = [0 for _ in range(can_learn)]
    max_result = 0
    
    def recur(X):
        global max_result

        if X == can_learn:
            cnt = 0
            str_set = sorted(arr_i, reverse=False)
            str_set = ''.join(str_set)

            for word in str_arr: # 'r' , 'hello', 'r'
                str_second_set = sorted(word, reverse=False)
                str_second_set = ''.join(str_second_set)
                result_1 = set(str_set)
                result_2 = set(str_second_set)
                
                result = result_2 - result_1
                if(len(result) == 0):
                    cnt += 1
                
                
            max_result = max(max_result, cnt)
            return

        for i in range(len(notyet_learn)):
            if checked[i] == False:
                checked[i] = True
                arr_i[X] = notyet_learn[i]
                recur(X+1)
                checked[i] = False
        return

    recur(0)

    print(max_result)
# str.replace('x','y') -> x를 y로 교체    