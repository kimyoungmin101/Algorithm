def solution(numbers, hand):
    answer = ''
    arr = [1,2,3,4,5,6,7,8,9,'*',0, '#']
    arr_result = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2],[3,0], [3,1], [3,2]]
    
    current_L = '*'
    current_R = '#'
    
    def distance(result_A, result_B):
        A = (arr_result[arr.index(result_A)])
        B = (arr_result[arr.index(result_B)])
        result = abs(B[0] - A[0]) + abs(B[1] - A[1])
        return result
    
    while(numbers):
        num = numbers.pop(0)
        if(num == 1 or num == 4 or num == 7):
            answer += 'L'
            current_L = num
        elif(num == 3 or num == 6 or num == 9):
            answer += 'R'
            current_R = num
        else:
            if(current_L == '*' and current_R == '#'):
                if(hand == 'left'):
                    answer += 'L'
                    current_L = num
                elif(hand == 'right'):
                    answer += 'R'
                    current_R = num
            else:
                left = distance(current_L, num)
                right = distance(current_R, num)
                if(left > right):
                    answer += 'R'
                    current_R = num
                elif(left < right):
                    answer += 'L'
                    current_L = num
                else:
                    if(hand == 'left'):
                        answer += 'L'
                        current_L = num
                    elif(hand == 'right'):
                        answer += 'R'
                        current_R = num
    return answer
