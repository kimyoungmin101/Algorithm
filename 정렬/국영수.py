# https://www.acmicpc.net/problem/10825

students = []

N = int(input())
for i in range(N):
    students.append(list(map(str, input().split())))
    students[i][1] = int(students[i][1])
    students[i][2] = int(students[i][2])
    students[i][3] = int(students[i][3])

if_bool = False

students = sorted(students, key = lambda X : (-X[1], X[2], -X[3], X[0]))


for i in students:
    print(i[0])
