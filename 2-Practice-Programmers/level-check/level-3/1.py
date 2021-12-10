# (탐욕) B팀의 낮은 숫자부터 이길수 있는지 확인

import collections


def solution(ateam, bteam):
    ateam = collections.deque(sorted(ateam))
    bteam = sorted(bteam)

    wins = 0
    for x in bteam:
        if x > ateam[0]:
            wins += 1
            ateam.popleft()

    return wins


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))  # 3
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))  # 0
