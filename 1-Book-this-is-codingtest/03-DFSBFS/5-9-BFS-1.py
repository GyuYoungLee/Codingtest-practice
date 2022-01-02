# [BFS]

import collections

N = 4
graph = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
S = 1

qu = collections.deque([S])
dist = [-1] * (N + 1)  # 거리 테이블
dist[S] = 0

while qu:
    now = qu.popleft()
    print(now, end=' ')  # 탐색

    for e in graph[now]:
        if dist[e] == -1:
            dist[e] = dist[now] + 1
            qu.append(e)
