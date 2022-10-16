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
visited = [0] * (n + 1)  # 방문 테이블

qu = collections.deque([s])
visited[s] = 1

while qu:
    v = qu.popleft()
    print(v)

    for e in graph[v]:
        if not visited[e]:
            qu.append(e)
            visited[e] = 1
