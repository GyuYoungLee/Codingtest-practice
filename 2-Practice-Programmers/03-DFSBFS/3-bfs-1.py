# [단어 변환] 최소 변환 단계 (bfs)

# 탐색방향: 간선
# 탐색조건: visited[e] == 0
# 탐색결과: visited[e] = 1

import collections


def is_possible(w1, w2):
    d = collections.Counter(w1) - collections.Counter(w2)
    return True if len(list(d.keys())) == 1 else False


def solution(begin, target, words):
    graph = collections.defaultdict(list)
    visited = collections.defaultdict(int)

    for w in [begin] + words:
        for e in [x for x in [begin] + words if is_possible(w, x)]:
            graph[w].append(e)
        visited[w] = 0

    qu = collections.deque([(begin, 0)])
    visited[begin] = 1

    while qu:
        w, count = qu.popleft()
        if w == target:
            return count

        for e in graph[w]:
            if not visited[e]:
                visited[e] = 1
                qu.append((e, count + 1))

    return 0


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))  # 0
