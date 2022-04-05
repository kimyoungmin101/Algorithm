from collections import deque

def move_down(dice_arr):
    dice_arr.rotate(1)
    return dice_arr

def move_up(dice_arr):
    dice_arr.rotate(-1)
    return dice_arr

def move_right(dice_arr):
    for i in range(len(dice_arr)):
        A = deque(dice_arr[i])
        A.rotate(1)
        
        for j in range(len(A)):
            dice_arr[i][j] = A[j]
            
    return dice_arr

def move_left(dice_arr):
    for i in range(len(dice_arr)):
        A = deque(dice_arr[i])
        A.rotate(-1)
        
        for j in range(len(A)):
            dice_arr[i][j] = A[j]
            
    return dice_arr

dice = [[1+_,2+_,3+_] for _ in range(5)]

dice = deque(dice)

for i in dice:
    print(i)
print(' ')

dice = move_down(dice)

for i in dice:
    print(i)
    
print(' ')

dice = move_up(dice)

for i in dice:
    print(i)
    
print(' ')

dice = move_right(dice)

for i in dice:
    print(i)
    
print(' ')

dice = move_left(dice)

for i in dice:
    print(i)
    
print(' ')