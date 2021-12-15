# [단어 변환] 최소 변환 단계 (bfs)

# 탐색방향: 알파벳차이 1개
# 탐색조건: e not in visited
# 탐색결과: visited.append(e)

import collections


def is_possible(w1, w2):
    d = collections.Counter(w1) - collections.Counter(w2)
    return True if len(list(d.keys())) == 1 else False


def solution(begin, target, words):
    qu = collections.deque([(begin, 0)])
    visited = [begin]

    while qu:
        w, count = qu.popleft()
        if w == target:
            return count

        for e in [x for x in words if is_possible(w, x)]:
            if e not in visited:
                visited.append(e)
                qu.append((e, count + 1))

    return 0


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))  # 0
