# [디스크 콘트롤러] 요청부터 종료까기 걸리는 최소 평균시간 (힙)

# 소요시간이 작은 순서로 처리하기 위해 힙 사용

import heapq
import collections


def solution(jobs):
    # 요청시간, 소요시간이 작은 순서로 정렬
    jobs = sorted(jobs)
    jobs = collections.deque(jobs)
    n = len(jobs)

    # jobs: [[0, 3], [1, 9], [2, 6]]
    # 가장 먼저 요청된 작업 1개를 힙에 넣는다
    qu = []
    t, w = jobs.popleft()
    heapq.heappush(qu, (w, t))

    current = t
    waited = 0

    while qu:
        w, t = heapq.heappop(qu)
        current += w
        waited += current - t

        # 현재시간까지 요청된 작업을 추가로 힙에 추가한다
        while jobs and jobs[0][0] <= current:
            t, w = jobs.popleft()
            heapq.heappush(qu, (w, t))

        # 현재시간까지 요청된 작업이 없다면 가장 먼저 요청된 작업 1개를 힙에 넣는다
        if jobs and not qu:
            t, w = jobs.popleft()
            heapq.heappush(qu, (w, t))
            current = t

    return waited // n


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
