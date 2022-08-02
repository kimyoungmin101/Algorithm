# 문자열 압축

def solution(s):
    answer = 0
    cnt = (len(s) // 2)
    
    min_result = 10000000
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        return 2
    
    for i in range(1, cnt+1):
        previous = ''
        as_result = ''
        cnt_value = 1
        
        for j in range(0, len(s), i):
            value = s[j:j+i]
            if previous == '':
                previous = value
            elif previous == value:
                cnt_value += 1
            else:
                if cnt_value == 1:
                    as_result += previous
                else:
                    as_result += (str(cnt_value) + previous)
                previous = value
                cnt_value = 1
        if cnt_value == 1:
            as_result += previous
        else:
            as_result += (str(cnt_value) + previous)
        min_result = min(len(as_result), min_result)
        
        # ababcdcdababcdcd
    return min_result