# 알고리즘 교재 P382

A = str(input())
B = str(input())

arr_A = list(map(str, A.strip()))
arr_B= list(map(str, B.strip()))


def edit_dist(X, Y):

    word_arr = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

    for i in range(1, len(Y)+1):
        word_arr[0][i] = i
    for i in range(1, len(X)+1):
        word_arr[i][0] = i

    
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i-1] == Y[j-1]:
                word_arr[i][j] = word_arr[i-1][j-1]
            else:
                word_arr[i][j] = 1 + min(word_arr[i-1][j-1], word_arr[i-1][j], word_arr[i][j-1])    
    # 알파벳이 같으면 arr[-1][-1] 그대로 가져오기
    # 다르면 arr[i-1][j], arr[i-1][j], arr[i-1][j-1] 중 최소값 + 1 가져오기

    return word_arr[-1][-1]

print(edit_dist(arr_A, arr_B))



'''
sunday
saturday
'''

