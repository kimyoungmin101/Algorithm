# 기둥과 보설치

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

def possible(result):
    for x,y,a in result:
        if a == 0: # 기둥인 경우
            if (y == 0) or ([x-1,y,1] in result) or ([x,y, 1] in result) or ([x, y-1, 0] in result):
                continue
            else:
                return False
        else: # 보인 경우
            if ([x,y-1,0] in result) or ([x+1,y-1,0] in result) or (([x-1, y, 1] in result) and ([x+1,y,1] in result)):
                continue
            else:
                return False
    return True
    
def solution(n, build_frame):
    stack = []
    
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            stack.append([x,y,a])
            if possible(stack):
                continue
            stack.remove([x,y,a])
        else: # 삭제
            stack.remove([x,y,a])
            if possible(stack):
                continue
            stack.append([x,y,a])
        
    stack = sorted(stack, key = lambda X : (X[0], X[1], X[2]))
    return stack