# [이중 우선순위큐] 모든 연산 후의 큐의 최대값, 최소값 (힙)

# 최대값, 최소값 꺼내기 위해 2개의 힙 사용

import heapq


def solution(arr):
    max_heap = []
    min_heap = []

    for x in arr:
        op, num = x.split()
        num = int(num)

        # 넣기
        if op == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)

        # 꺼내기
        else:
            if num == 1:
                if max_heap:
                    heapq.heappop(max_heap)
            else:
                if min_heap:
                    heapq.heappop(min_heap)

            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다
            if not min_heap or not max_heap or min_heap[0] > -max_heap[0]:
                max_heap = []
                min_heap = []

    # 큐가 비어 있다면
    if not max_heap or not min_heap:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]


print(solution(["I 16", "D 1"]))  # [0, 0]
print(solution(["I 7", "I 5", "D 1", "D -1"]))  # [7, 5]
