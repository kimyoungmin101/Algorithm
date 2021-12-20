input_num = int(input())

line = 0  # 사선 라인
max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
while input_num > max_num:
    line += 1  
    max_num += line  


gap = max_num - input_num 

if(line % 2 == 0):
    print(f'{line - gap}/{1 + gap}')
else:
    print(f'{1 + gap}/{line - gap}')

