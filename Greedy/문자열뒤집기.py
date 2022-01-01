str_s = list(map(str, input().strip()))
result = 0
if '0' not in str_s:
    print(0)
elif '1' not in str_s:
    print(0)
else:
    zero_cnt = 0
    one_cnt = 0
    zero_bool = False
    one_bool = False

    for i in str_s:
        if i == '0':
            if zero_bool == False:
                one_bool = False
                zero_bool = True
                zero_cnt += 1
        elif i == '1':
            if one_bool == False:
                zero_bool = False
                one_bool = True
                one_cnt += 1
    result = min(zero_cnt, one_cnt)

    print(result)


'''
11001100110011000001
0110000000101
'''
