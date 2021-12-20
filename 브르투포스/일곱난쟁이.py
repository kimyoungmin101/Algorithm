heights = []

for i in range(9):
    heights.append(int(input()))

heights.sort()

def find_people(heights):
    N = 9

    
    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue
            copy_heights = heights.copy()
            copy_heights.pop(i)
            copy_heights.pop(j-1)
            if sum(copy_heights) == 100:
                return copy_heights

result = find_people(heights)

for i in result:
    print(i)