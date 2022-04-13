# https://www.acmicpc.net/problem/5373

def rotate_90(cube):
    cube = list(zip(*cube[::-1]))
    for i in range(len(cube)):
        cube[i] = list(cube[i])
    
    return cube

def result_leftright(cube):
    result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            result[i][j] = cube[i+9][j+3]
    
    arr_zero = result[0]
    arr_one = result[1]
    arr_two = result[2]
    
    new_result = [[0 for _ in range(3)] for _ in range(3)]
    
    new_result[0] = arr_two
    new_result[1] = arr_one
    new_result[2] = arr_zero
    
    arr_zero = []
    arr_one = []
    arr_two = []
    
    for i in range(3):
        new_result[i][0], new_result[i][2] = new_result[i][2], new_result[i][0]
            
    for i in range(3):
        for j in range(3):
            cube[i+3][j+9] = new_result[i][j]
    
    return cube

def result_updown(cube):
    result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            result[i][j] = cube[i+3][j+9]
    
    for i in range(3):
        result[i][0], result[i][2] = result[i][2], result[i][0]
        
    arr_zero = result[0]
    arr_one = result[1]
    arr_two = result[2]
    
    new_result = [[0 for _ in range(3)] for _ in range(3)]
    
    new_result[0] = arr_two
    new_result[1] = arr_one
    new_result[2] = arr_zero
    
    for i in range(3):
        for j in range(3):
            cube[i+9][j+3] = new_result[i][j]
    
    return cube

def rotate_up(direction, cube):
    arr = cube[3]
    up_result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            up_result[i][j] = cube[i][j+3]
            
    if direction == '+':
        up_result = rotate_90(up_result)
    else:
        up_result = rotate_90(up_result)
        up_result = rotate_90(up_result)
        up_result = rotate_90(up_result)

    for i in range(3):
        for j in range(3):
            cube[i][j+3] = up_result[i][j]
            
    for i in range(3):
        new_arr = [0 for _ in range(len(arr))]
        if direction == '-':
            for i in range(len(arr)-1):
                new_arr[i+1] = arr[i]
            new_arr[0] = arr[len(arr)-1]
        else:
            for i in range(len(arr)-1):
                new_arr[i] = arr[i+1]
            new_arr[len(arr)-1] = arr[0]
        arr = new_arr
        
    cube[3] = arr
    
    cube = result_updown(cube)
    
    return cube


def rotate_down(direction, cube):
    arr = cube[5]
    down_result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            down_result[i][j] = cube[i+6][j+3]
            
    if direction == '+':
        down_result = rotate_90(down_result)
    else:
        down_result = rotate_90(down_result)
        down_result = rotate_90(down_result)
        down_result = rotate_90(down_result)
    
    for i in range(3):
        for j in range(3):
            cube[i+6][j+3] = down_result[i][j]
            
    for i in range(3):
        new_arr = [0 for _ in range(len(arr))]
        if direction == '+':
            for i in range(len(arr)-1):
                new_arr[i+1] = arr[i]
            new_arr[0] = arr[len(arr)-1]
        else:
            for i in range(len(arr)-1):
                new_arr[i] = arr[i+1]
            new_arr[len(arr)-1] = arr[0]
        arr = new_arr
        
    cube[5] = arr
    
    cube = result_updown(cube)
    
    return cube

def rotate_left(direction, cube):    
    left_result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            left_result[i][j] = cube[i+3][j]
    if direction == '+':
        left_result = rotate_90(left_result)
    else:
        left_result = rotate_90(left_result)
        left_result = rotate_90(left_result)
        left_result = rotate_90(left_result)
    
    for i in range(3):
        for j in range(3):
            cube[i+3][j] = left_result[i][j]
            
    cube = rotate_90(cube)
    arr = cube[3]   

    for i in range(3):
        new_arr = [0 for _ in range(len(arr))]
        if direction == '-':
            for i in range(len(arr)-1):
                new_arr[i+1] = arr[i]
            new_arr[0] = arr[len(arr)-1]
        else:
            for i in range(len(arr)-1):
                new_arr[i] = arr[i+1]
            new_arr[len(arr)-1] = arr[0]
        arr = new_arr
        
    cube[3] = arr
    
    cube = rotate_90(cube)
    cube = rotate_90(cube)
    cube = rotate_90(cube)
    
    cube = result_leftright(cube)
    
    return cube
    

def rotate_right(direction, cube):
    right_result = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            right_result[i][j] = cube[i+3][j+6]
    if direction == '+':
        right_result = rotate_90(right_result)
    else:
        right_result = rotate_90(right_result)
        right_result = rotate_90(right_result)
        right_result = rotate_90(right_result)
    
    for i in range(3):
        for j in range(3):
            cube[i+3][j+6] = right_result[i][j]
            
    cube = rotate_90(cube)
    arr = cube[5]
    
    for i in range(3):
        new_arr = [0 for _ in range(len(arr))]
        if direction == '+':
            for i in range(len(arr)-1):
                new_arr[i+1] = arr[i]
            new_arr[0] = arr[len(arr)-1]
        else:
            for i in range(len(arr)-1):
                new_arr[i] = arr[i+1]
            new_arr[len(arr)-1] = arr[0]
            
        arr = new_arr
        
    cube[5] = arr
    
    cube = rotate_90(cube)
    cube = rotate_90(cube)
    cube = rotate_90(cube)
    
    cube = result_leftright(cube)
    
    return cube

def rotate_front(direction, cube):
    result = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            result[i][j] = cube[i+2][j+2]
    
    if direction == '+':
        result = rotate_90(result)
    else:
        result = rotate_90(result)
        result = rotate_90(result)
        result = rotate_90(result)
    
    for i in range(5):
        for j in range(5):
            cube[i+2][j+2] = result[i][j]
            
    return cube

def rotate_back(direction, cube): #수정해보기
    result = [[0 for _ in range(9)] for _ in range(9)]
    
    real_back = [[0 for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            real_back[i][j] = cube[i+9][j+3]
    
    real_back[0], real_back[2] = real_back[2], real_back[0]
    
    if direction == '+':
        real_back = rotate_90(real_back)
        real_back = rotate_90(real_back)
        real_back = rotate_90(real_back)
    else:
        real_back = rotate_90(real_back)
    
    real_back[0], real_back[2] = real_back[2], real_back[0]
    
    for i in range(9):
        for j in range(9):
            result[i][j] = cube[i][j]
    if direction == '-':
        result = rotate_90(result)
    else:
        result = rotate_90(result)
        result = rotate_90(result)
        result = rotate_90(result)        
    
    for i in range(9):
        for j in range(9):
            if i == 0 or j == 0 or i == 8 or j == 8:
                cube[i][j] = result[i][j]
    
    for i in range(3):
        for j in range(3):
            cube[i+9][j+3] = real_back[i][j]
        
    cube = result_leftright(cube)   
    
    return cube


def firstState():
    cube = [['|' for _ in range(12)] for _ in range(12)]
    for i in range(3):
        for j in range(3):
            cube[i][j+3] = 'w'
    
    for i in range(3):
        for j in range(3):
            cube[i+3][j] = 'g'
    
    for i in range(3):
        for j in range(3):
            cube[i+3][j+3] = 'r'
            
    for i in range(3):
        for j in range(3):
            cube[i+3][j+6] = 'b'
            
    for i in range(3):
        for j in range(3):
            cube[i+3][j+9] = 'o'
            
    for i in range(3):
        for j in range(3):
            cube[i+6][j+3] = 'y'
    
    for i in range(3):
        for j in range(3):
            cube[i+9][j+3] = 'o'
            
    return cube

def turn(direct, cube):
    if direct[0] == 'U':
        cube = rotate_up(direct[1], cube) # +, cube
    elif direct[0] == 'D':
        cube = rotate_down(direct[1], cube) # +, cube
    elif direct[0] == 'F':
        cube = rotate_front(direct[1], cube) # +, cube
    elif direct[0] == 'B':
        cube = rotate_back(direct[1], cube) # +, cube
    elif direct[0] == 'L':
        cube = rotate_left(direct[1], cube) # +, cube
    elif direct[0] == 'R':
        cube = rotate_right(direct[1], cube) # +, cube
    
    return cube

N = int(input())
ans = []
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
for i in range(N):
    cnt = int(input())
    arr = list(map(str, input().split()))
    
    cube = firstState()
    
    for j in arr:
        cube = turn(j, cube)
        
    
    for i in range(3):
        str_s = cube[i][3] + cube[i][4] + cube[i][5]
        ans.append(str_s)
# U+ B- R- F- D+ L- B+ U-

for i in ans:
    print(i)