# [무지의 먹방 라이브] 섭취 순서가 되는 음식의 번호 (탐욕)

import heapq


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    qu = []
    for i, x in enumerate(food_times):
        heapq.heappush(qu, (x, i + 1))

    n = len(qu)
    pre = 0

    while k - (qu[0][0] - pre) * n >= 0:
        now = heapq.heappop(qu)[0]
        k -= (now - pre) * n  # 모든 음식을 한번에 감소시킨다

        n -= 1
        pre = now

    remain = sorted(qu, key=lambda x: x[1])
    return remain[k % n][1]


print(solution([3, 1, 2], 5))  # 1
