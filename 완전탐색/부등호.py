N = int(input())
arrow = list(map(str, input().split()))

'''
2
< >

897
021


'''
visited = [False for _ in range(10)] #
min_result_arr = [0 for _ in range(N+1)] # [0 0 0]
min_result = '9' * (N+1)
max_result = '0' * (N+1)

max_result = int(max_result)
min_result = int(min_result)

arr_result = []

def recursive(X):

    if X == N+1:
        for i in range(1, len(min_result_arr)):
            if arrow[i-1] == '<' and min_result_arr[i-1] < min_result_arr[i]:
                pass
            elif arrow[i-1] == '>' and min_result_arr[i-1] > min_result_arr[i]:
                pass
            else:
                break
            
            if i == len(min_result_arr) - 1:
                global max_result
                global min_result
                min_result_int = int(min_result)
                max_result_int = int(max_result)

                answer = min_result_arr.copy()
                answer = list(map(str, answer))
                answer = "".join(answer)
                answer_int = int(answer)
                if answer_int < min_result_int:
                    min_result = answer
                if answer_int > max_result_int:
                    max_result = answer
                
        return
    
    for i in range(10):
        if visited[i] == False:
            min_result_arr[X] = i
            visited[i] = True
            recursive(X+1)
            visited[i] = False

    return

recursive(0)
print(max_result)
print(min_result)
