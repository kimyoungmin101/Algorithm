# 괄호변환

def solution(p):
    answer = ''
    if p == "":
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    
    def collect(word):
        stack = []
        for i in word:
            if len(stack) == 0:
                stack.append(i)
            else:
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False
    
    # 만약 p가 이미 "올바른 괄호 문자열"이라면 그대로 return 하면 됩니다.
    if collect(p):
        return p
    
    real_u = ""
    
    def dfs(new_word):   
        
        u = []
        v = ""
        cnt = 0
        if new_word == "":
            return ""
        
        for i in range(len(new_word)):
            u.append(new_word[i])
            if u.count("(") == u.count(")"):
                cnt = i
                break
        u = "".join(u)
        
        if cnt + 1 < len(new_word):
            v = new_word[cnt+1:]     
        elif len(u) == len(new_word):
            v = ""
        
        if collect(u): #올바른 괄호 문자열 이라면
            return u + dfs(v)
        else:
            bin_str = "("
            bin_str += dfs(v)
            bin_str += ")"
            u = u[1:]
            u = u[:-1]
            ans = ""
            for i in u:
                if i == "(":
                    ans += ")"
                else:
                    ans += "("
            return bin_str + ans
        
    answer = dfs(p)
    
    return answer

