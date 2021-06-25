import re

def solution(new_id):
    answer = new_id.lower() # lower => 소문자 변환!!
    answer = re.sub('[^a-z0-9\.\_\-]', '', answer)
    # re.sub는 첫번째 ''에 있는 조건을 두번째 ''으로 바꿔주는 역할을 한다
    answer = re.sub('\.+', '.', answer)
    if(answer[0] == '.'):
        answer = answer[1:]
    
    if(answer[-1:] == '.'):
        answer = answer[:-1]
    
    if(len(answer) == 0):
        answer = 'aaa'
    
    if(len(answer) >= 16):
        answer = answer[:15]
    
    if(answer[-1:] == '.'):
        answer = answer[:-1]
    
    if(len(answer) <= 2):
        while(len(answer) < 3):
            answer += answer[-1:]
    return answer
