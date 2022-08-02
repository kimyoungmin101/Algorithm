def attach(new_key, new_arr, X, Y):
    for i in range(len(new_key)):
        for j in range(len(new_key)):
            new_arr[i+X][j+Y] += new_key[i][j]
    return new_arr

def detach(new_key, new_arr, X, Y):
    for i in range(len(new_key)):
        for j in range(len(new_key)):
            new_arr[i+X][j+Y] -= new_key[i][j]
    return new_arr

def find(new_arr, X, Y, len_lock):
    for i in range(len_lock):
        for j in range(len_lock):
            if new_arr[i+X][j+Y] != 1:
                return False
    return True
    
def solution(key, lock):    
    arr = [[0 for _ in range(((len(key)-1) * 2) + len(lock))] for _ in range(((len(key)-1) * 2) + len(lock))]
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            arr[i+len(key)-1][j+len(key)-1] = lock[i][j]
    
    # key = list(zip(*key[::-1]))
    
    for i in range(len(arr) - len(key) + 1):
        for j in range(len(arr) - len(key) + 1):
            for k in range(4):
                key = list(zip(*key[::-1]))
                arr = attach(key, arr, i, j)
                if find(arr, len(key)-1, len(key)-1, len(lock)):
                    return True
                arr = detach(key, arr, i, j)
                
    return False