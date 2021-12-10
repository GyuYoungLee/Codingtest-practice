# [기능개발] 각 배포마다 몇개 기능이 배포되는지 리턴 (큐)

import collections
import math


def solution(progresses, speeds):
    # 완료일 리스트
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))

    # 배포갯수 리스트: qu [7, 3, 9] => result [2, 1]
    result = []
    qu = collections.deque(days)

    while qu:
        x = qu.popleft()
        count = 1

        while qu and qu[0] <= x:
            qu.popleft()
            count += 1

        result.append(count)

    return result


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]