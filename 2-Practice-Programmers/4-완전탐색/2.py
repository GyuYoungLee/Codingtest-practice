# [소수 찾기] 소수를 몇개 만들수 있는지 (완전탐색, itertools)

import itertools


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    numbers = list(numbers)
    n = len(numbers)

    # (완전탐색) 만들수 있는 숫자들 탐색
    result = set()
    for i in range(1, n + 1):
        for arr in itertools.permutations(numbers, i):
            result.add(int("".join(arr)))

    # 소수가 아닌 값들 제거
    for x in list(result):
        if not is_prime(x):
            result.remove(x)

    return len(result)


print(solution("17"))  # 3
print(solution("011"))  # 2
