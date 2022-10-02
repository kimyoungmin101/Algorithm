stack = [1,2,3,4,5]
idx = stack.index(3)

left_stack = stack[:idx]
right_stack = stack[idx:]

print(left_stack)
print(right_stack)
