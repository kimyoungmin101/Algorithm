import heapq

width = 3
height = 3
diamond = [[1,1],[2,2]]

stop = []
start = [height, 0]
end = [0, width]

def get_result(arr, start, middle, end):
    real_middle = []
    result = 0
    dx = [0,-1]
    dy = [1,0]
    heap = []
        
    arr[start[0]][start[1]] = 1
    
    heapq.heappush(heap, start) # 2,0
    
    while heap:
        X, Y = heapq.heappop(heap)
        for k in range(2):
            real_X = X + dx[k]
            real_Y = Y + dy[k]
            if real_X < 0 or real_Y < 0 or real_X >= len(arr) or real_Y >= len(arr[0]):
                continue
            if real_Y - 1 < 0 or real_X + 1 >= len(arr):
                arr[real_X][real_Y] = arr[X][Y]
            else:
                arr[real_X][real_Y] = arr[real_X][real_Y-1] + arr[real_X+1][real_Y]
            heapq.heappush(heap, [real_X, real_Y])
    
   
    for i in range(len(middle)):
        in_result = 0
        X = middle[i][0]
        Y = middle[i][1]
        in_result = arr[X][Y]
        if i == 0:
            real_middle = middle[1]
        else:
            real_middle = middle[0]
        
        print('ㅡㅡㅡㅡㅡㅡ')    
        for i in arr:
            print(i)
        print(' ')
        
        second_arr = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
        second_arr[real_middle[0]][real_middle[1]] = 1
        heap = []
        heapq.heappush(heap, real_middle)
        
        while heap:
            X, Y = heapq.heappop(heap)
            for k in range(2):
                real_X = X + dx[k]
                real_Y = Y + dy[k]
                if real_X < 0 or real_Y < 0 or real_X >= len(second_arr) or real_Y >= len(second_arr[0]):
                    continue
                if real_Y - 1 < 0 or real_X + 1 >= len(second_arr):
                    second_arr[real_X][real_Y] = second_arr[X][Y]
                else:
                    second_arr[real_X][real_Y] = second_arr[real_X][real_Y-1] + second_arr[real_X+1][real_Y]
                heapq.heappush(heap, [real_X, real_Y])
        
        in_result *= second_arr[end[0]][end[1]]
        
        for i in second_arr:
            print(i)
        print('ㅡㅡㅡㅡㅡㅡㅡㅡ', in_result)
        result += in_result

    return result

for i in diamond:
    ans = []
    dx = start[0] - i[0]
    dy = start[1] + i[1]
    ans.append([dx+1, dy])
    ans.append([dx, dy-1])
    
    stop.append(ans)

result = 0

for i in stop:
    arr = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    result += get_result(arr, start, i, end)

print(result)