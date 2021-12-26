# [국영수] 조건에 따라 학생들 정렬 (정렬)

import sys

n = int(input())

student = []
for _ in range(n):
    name, ko, en, math = sys.stdin.readline().rstrip().split()
    student.append((int(ko), int(en), int(math), name))

student.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))  # 정렬

for ko, en, math, name in student:
    print(name)
