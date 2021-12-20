def solution(nums):
    answer = 0
    answer = len(nums) // 2
    
    nums = set(nums)
    nums = list(nums)
    

    if(answer > len(nums)):
        return len(nums)
    else:
        return answer
    
    return answer
