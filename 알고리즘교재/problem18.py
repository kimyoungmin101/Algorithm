# https://programmers.co.kr/learn/courses/30/lessons/60058 (괄호 변환)

def divide(w):
    left_cnt = 0
    right_cnt = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            left_cnt += 1
        else:
            right_cnt += 1
            
        if left_cnt == right_cnt:
            return w[:i+1], w[i+1:]

def collectStr(u):
    stack = []
    for i in range(len(u)):
        if len(stack) == 0:
            stack.append(u[i])
        else:
            if stack[-1] == '(' and u[i] == ')':
                stack.pop()
            else:
                stack.append(u[i])
    
    stack = ''.join(stack)
    
    return stack

def solution(p):
    # 조건 1
    if p == '':
        return ''
    
    def recursive(w):
        # 조건 1
        if w == '':
            return ''
        
        # 조건 2
        u, v = divide(w)
        
        # 조건 3 올바른 괄호 문자열이라면
        stack_result = collectStr(u)
        
        if stack_result == '':
            u += recursive(v)
            return u
        else:
            # 4-1
            bin_str = '('
            # 4-2
            bin_str += recursive(v)
            # 4-3
            bin_str += ')'
            # 4-4
            u = u[1:]
            u = u[:-1]
            
            for i in u:
                if i == '(':
                    bin_str += ')'
                else:
                    bin_str += '('
            return bin_str
        
    print(recursive(p))
        
    answer = ''
    return answer
    
solution("))((()")