# [소수찾기] 소수를 몇개 만들수 있는지 (완전탐색, itertools)

# 성능 개선을 위해 에라토네스의 체 사용

import itertools


def solution(numbers):
    numbers = list(numbers)
    n = len(numbers)

    result = set()
    for i in range(1, n + 1):
        result |= set(map(int, map(''.join, itertools.permutations(numbers, i))))

    # 소수가 아닌 값들 제거 (에라토네스의 체)
    result -= {0, 1}
    for i in range(2, int(max(result) ** 0.5) + 1):
        result -= set(range(i + i, max(result) + 1, i))

    return len(result)


print(solution("17"))  # 3
print(solution("011"))  # 2
