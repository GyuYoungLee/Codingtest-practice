# BFS

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
visited = [0] * (N + 1)  # 방문여부 테이블
visited[S] = 1

while qu:
    node = qu.popleft()
    print(node, end=' ')  # 탐색

    for e in graph[node]:
        if not visited[e]:
            visited[e] = 1
            qu.append(e)
