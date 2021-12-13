# [국영수] 조건에 따라 학생들 정렬 (정렬)

import sys

n = int(input())

student = []
for _ in range(n):
    name, a, b, c = sys.stdin.readline().rstrip().split()
    student.append((int(a), int(b), int(c), name))

student.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

for a, b, c, name in student:
    print(name)
