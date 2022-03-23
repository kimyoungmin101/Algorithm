from collections import deque
import copy

def solution(topping, tasting):
    answer = 0
    
    start = tasting[0]
    min_idx = len(topping)
    
    left_rotate = copy.deepcopy(topping)
    right_rotate = copy.deepcopy(topping)
    
    left_cnt = 0
    right_cnt = 0
    
    queue = [[topping, 0]]
    
    min_answer = len(topping)
    start = tasting[0]
    cnt = 0
    
    while tasting:
        start = tasting.pop(0)
        new_queue = []

        for i in queue:
            new_topping, time = i[0], i[1]

            if new_topping[0] == start:
                new_queue.append([new_topping, time])
                continue

            left_rotate = copy.deepcopy(new_topping)
            right_rotate = copy.deepcopy(new_topping)
        
            left_rotate = deque(left_rotate)
            right_rotate = deque(right_rotate)
            
            for i in range(1, len(topping) // 2):
                left_rotate.rotate(-1)
                if left_rotate[0] == start:
                    left_sum_count = time + i
                    new_queue.append([left_rotate, left_sum_count])
                    break
            
            for i in range(1, len(topping) // 2):
                right_rotate.rotate(1)
                if right_rotate[0] == start:
                    right_sum_count = time + i
                    new_queue.append([right_rotate, right_sum_count])
                    break
        
        queue = copy.deepcopy(new_queue)

    queue = sorted(queue, key = lambda X : X[1])
    
    answer = queue[0][1]
    
    return answer


solution([2, 1, 3, 1, 2, 4, 4, 3], [3, 1, 2, 4])

