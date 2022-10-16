# [BFS]

import collections

n = 4
graph = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3]
]

s = 1
dist = [-1] * (n + 1)  # 방문 테이블

qu = collections.deque([s])
dist[s] = 0

while qu:
    v = qu.popleft()
    print(v)

    for e in graph[v]:
        if dist[e] == -1:
            qu.append(e)
            dist[e] = dist[v] + 1

print(dist)
