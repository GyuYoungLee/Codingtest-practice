# [외벽 점검] 취약지점을 점검하기 위해 필요한 친구의 최소값 (구현, 완전탐색=순열)

import itertools


def get_count(s_pos, m, weak, dist):
    cnt = 1
    covered = weak[s_pos] + dist[cnt - 1]

    for i in range(1 + s_pos, m + s_pos):
        if weak[i] <= covered:
            continue

        cnt += 1
        if cnt <= len(dist):
            covered = weak[i] + dist[cnt - 1]

    return cnt


def solution(n, weak, dist):
    m = len(weak)

    # (TIP) 점검 시작위치를 바꿔보기 위해 weak를 2배 늘린다
    weak += [x + n for x in weak]

    # 친구 순서를 바꾸어가며 탐색
    min_v = int(1e9)
    for candidates in itertools.permutations(dist, len(dist)):

        # 점검 시작위치를 바꾸어가며 탐색
        for s_pos in range(m):
            cnt = get_count(s_pos, m, weak, candidates)  # 투입되는 친구수
            min_v = min(min_v, cnt)

    return min_v if min_v <= len(dist) else -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # 2
