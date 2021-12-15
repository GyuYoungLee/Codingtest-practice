# [외벽 점검] 취약지점을 점검하기 위해 필요한 친구의 최소값 (구현, 완전탐색=순열)

import itertools


def solution(n, weak, dist):
    m = len(weak)
    weak += [x + n for x in weak]

    def get_count(i, friends):
        cnt = 1
        covered = weak[i] + friends[cnt - 1]

        for i in range(i + 1, i + m):
            if covered >= weak[i]:
                continue
            cnt += 1
            if cnt <= len(friends):
                covered = weak[i] + friends[cnt - 1]
        return cnt

    min_v = int(1e9)

    # 친구순서를 바꾸어가며 탐색
    for candidates in itertools.permutations(dist, len(dist)):

        # 점검 시작위치를 바꾸어가며 탐색
        for stat_idx in range(m):
            c = get_count(stat_idx, candidates)  # 필요한 친구수
            min_v = min(min_v, c)

    return min_v if min_v <= len(dist) else -1


print(solution(12, [1, 5, 6, 10], [3, 2, 1, 4]))
