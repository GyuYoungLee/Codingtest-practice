# [더 맵게] 섞어야 하는 최소횟수 (힙)

# 스코빌지수가 낮은 2개 음식을 추출하기 위해 횝 사용

import heapq


def solution(arr, target):
    qu = []
    for x in arr:
        heapq.heappush(qu, x)

    count = 0
    while len(qu) >= 2:
        n1 = heapq.heappop(qu)
        n2 = heapq.heappop(qu)
        heapq.heappush(qu, n1 + n2 * 2)
        count += 1

        if all(x >= target for x in qu):
            return count

    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 리턴합니다
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
