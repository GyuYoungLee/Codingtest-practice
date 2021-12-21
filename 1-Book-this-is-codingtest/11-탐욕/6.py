# [무지의 먹방 라이브] 섭취 순서가 되는 음식의 번호 (탐욕)

import heapq


def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    qu = []
    for i, x in enumerate(food_times):
        heapq.heappush(qu, (x, i + 1))

    pre = 0
    while k - len(qu) * (qu[0][0] - pre) >= 0:
        w = len(qu)
        h = heapq.heappop(qu)[0] - pre
        k -= w * h

        pre = h

    remain = sorted(qu, key=lambda x: x[1])
    no = remain[k % len(remain)][1]
    return no


print(solution([3, 1, 2], 5))  # 1
