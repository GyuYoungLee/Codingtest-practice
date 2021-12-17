# [무지의 먹방 라이브] 섭취 순서가 되는 음식의 번호 (탐욕)

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    qu = []
    for i, v in enumerate(food_times):
        heapq.heappush(qu, [v, i + 1])  # 음식의 갯수, 번호

    n = len(qu)
    pre = 0

    while (qu[0][0] - pre) * n <= k:
        now = heapq.heappop(qu)[0]
        k -= (now - pre) * n

        n -= 1
        pre = now

    remain = sorted(qu, key=lambda x: x[1])
    return remain[k % n][1]


print(solution([3, 1, 2], 5))
