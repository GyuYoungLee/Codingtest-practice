# [프린터] 요청한 문서가 몇 번째로 인쇄되는지  (큐)

import collections


def solution(priorities, location):
    qu = collections.deque(enumerate(priorities))
    count = 0

    while qu:
        i, x = qu.popleft()

        if all(x >= xx for ii, xx in qu):
            count += 1
            if i == location:
                return count
        else:
            qu.append((i, x))


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
