# [기능개발] 각 배포마다 몇개 기능이 배포되는지 리턴 (큐)

import math


def solution(progresses, speeds):
    # 완료일 리스트
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))

    # 배포갯수 리스트: qu [7, 3, 9] => result [2, 1]
    result = []
    n = len(days)
    i = 0
    j = 1

    while i < n:
        count = 1
        while j < n and days[j] <= days[i]:
            count += 1
            j += 1

        result.append(count)
        i = j
        j = i + 1

    return result


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
