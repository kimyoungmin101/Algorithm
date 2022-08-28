import sys

min_result = sys.maxsize
max_result = 0

def dfs(num, result):
    global min_result, max_result
    
    for n in num:
        if int(n) % 2 == 1:
            result += 1
            
    if len(num) == 1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    elif len(num) == 2:
        new_num = str(int(num[0]) + int(num[1]))
        dfs(new_num, result)
    else:
        for i in range(1, len(num) - 1):
            for j in range(1, len(num) - 1):
                if i + j >= len(num):
                    continue
                ans = [i, j, len(num)-i-j]
                start = 0
                sum_result = 0
                for k in range(3):
                    sum_result += int(num[start:start+ans[k]])
                    start += ans[k]
                    
                dfs(str(sum_result), result)
    
def main():
    global max_result, min_result
    
    x = sys.stdin.readline().rstrip()
    dfs(x, 0)
    print(min_result,max_result)
    
if __name__ == "__main__":
    main()
