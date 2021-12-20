N = input()

arr = []

for i in range(len(N)):
    arr.append(int(N[i]))

arr = sorted(arr, reverse = True)

for i in arr:
    print(i, end="")
