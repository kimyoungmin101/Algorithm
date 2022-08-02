# 문자열 재정렬

str_A = str(input())
int_arr = []
str_arr = []

for i in str_A:
    try:
        A = int(i)
        int_arr.append(A)
    except:
        str_arr.append(i)
str_arr.sort()

result = ''.join(str_arr)
result_int = sum(int_arr)

result += str(result_int)

print(result)
