num = int(input())
a = list(map(int, input().split(" ")))
result = ["-1" for _ in range(num)]
stack = []
stack.append(0)
i = 1
for i in range(num):
    while stack and a[stack[-1]] < a[i]:
        result[stack[-1]] = str(a[i])
        stack.pop()

    stack.append(i)
    i += 1

print(" ".join(result))
