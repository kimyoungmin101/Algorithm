def solution(lottos, win_nums):
    answer = []
    ans = [6,6,5,4,3,2,1]
    zero_count = lottos.count(0)
    # 2 => 5, 3 => 4, 4 => 3, 5 => 2, 6 => 1
    count = 0
    
    for i in range(6):
        num = 0
        if(lottos[i] != 0):
            num = lottos[i]
            if num in win_nums:
                count += 1
    
    if(zero_count == 6):
        min_result = ans[count]
        max_result = 1
    else:
        min_result = ans[count]
        max_result = ans[count + zero_count]
    
    answer.append(max_result)
    answer.append(min_result)
            
        
    return answer
