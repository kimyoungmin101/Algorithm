# https://www.acmicpc.net/problem/16719

import sys
input = sys.stdin.readline
 
S = list(input().rstrip())
result = ['']*len(S)


'''
STARTLINK
'''
def divide_result(cnt_S, start):
    if start >= len(result) or len(cnt_S) == 0:
        return
    min_S = min(cnt_S)
    idx = cnt_S.index(min_S)
    
    result[start+idx] = min_S
    
    print(''.join(result))
    # RTLINK, 3
    divide_result(cnt_S[idx+1:], start+idx+1)
    divide_result(cnt_S[:idx], start)
    
divide_result(S, 0)