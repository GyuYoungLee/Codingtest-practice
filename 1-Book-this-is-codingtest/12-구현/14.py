# [외벽 점검] 취약지점을 점검하기 위해 필요한 친구의 최소값 (구현, 완전탐색=순열)

import itertools


def solution(n, weak, dist):
    # 필요한 친구수
    def get_count(start_idx, friends):
        cnt = 1
        covered = weak[start_idx] + friends[cnt - 1]

        for i in range(1 + start_idx, m + start_idx):
            if covered >= weak[i]:
                continue

            cnt += 1
            if cnt <= len(friends):
                covered = weak[i] + friends[cnt - 1]
        return cnt

    m = len(weak)
    f = len(dist)
    weak += [x + n for x in weak]

    # 친구 순서를 바꾸어가며 탐색
    min_v = int(1e9)
    for candidates in itertools.permutations(dist, f):

        # 점검 시작 위치를 바꾸어가며 탐색
        for start_idx in range(m):
            c = get_count(start_idx, candidates)
            min_v = min(min_v, c)

    return min_v if min_v <= f else -1


print(solution(12, [1, 5, 6, 10], [3, 2, 1, 4]))
