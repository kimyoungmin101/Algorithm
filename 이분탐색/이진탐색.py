from sys import stdin, stdout

N = int(stdin.readline())
N_arr = list(map(int, stdin.readline().split()))

Q = int(stdin.readline())
Q_arr = list(map(int, stdin.readline().split()))


def binary(start, N_arr, end, target):
    if(start > end):
        return -1

    mid = (start + end) # 2
    if(target == N_arr[mid]):
        return mid
    elif(target > N_arr[mid]):
        return binary(mid+1, N_arr, end, target)
    else:
        return binary(start, N_arr, mid-1, target)
    

start = 0
end = N - 1

for i in Q_arr:
    print(binary(start, N_arr, end, i), end=" ")