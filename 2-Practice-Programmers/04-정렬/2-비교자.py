# [가장 큰 수] 가장 큰수를 만들어서 문자열로 리턴 (정렬, comparator)

import functools


def comparator(x, y):
    n1 = int(x + y)
    n2 = int(y + x)
    return (n1 > n2) - (n1 < n2)  # n1이 크면 1, n2가 크면 -1, 같으면 0


def solution(numbers):
    a = list(map(str, numbers))
    a.sort(key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(a)))


print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
print(solution([30, 3021]))  # 303021 => 1-6 반례
print(solution([0, 0]))  # 0 => 18번 반례
