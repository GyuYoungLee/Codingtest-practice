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
dist = [-1] * (N + 1)  # 거리 테이블

qu = collections.deque([S])
dist[S] = 0

while qu:
    v = qu.popleft()
    print(v, end=' ')  # 탐색

    for e in graph[v]:
        if dist[e] == -1:
            qu.append(e)
            dist[e] = dist[v] + 1

print(dist)
