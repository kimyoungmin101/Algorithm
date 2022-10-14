from collections import deque
import sys

def solution(queue1, queue2):
    cnt = 0

    max_len = len(queue1) + len(queue2)
    
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    
    result = (sum_que1 + sum_que2) // 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
        
    while True:
        if len(queue1) == 0 or len(queue2) == 0 or cnt > max_len * 2:
            cnt = -1
            break
            
        if sum_que1 == sum_que2:
            break
        elif sum_que1 > sum_que2:
            A = queue1.popleft()
            queue2.append(A)
            sum_que1 -= A
            sum_que2 += A
            cnt += 1
        else:
            B = queue2.popleft()
            queue1.append(B)
            sum_que2 -= B
            sum_que1 += B
            cnt += 1
    
    return cnt
