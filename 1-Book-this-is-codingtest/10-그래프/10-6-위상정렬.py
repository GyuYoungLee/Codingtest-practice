# [위상 정렬] 진입차수가 0 이면 큐에 추가

import collections

N = 7
graph = [
    [],
    [2, 5],
    [3, 6],
    [4],
    [7],
    [6],
    [4],
    []
]
S = 1

qu = collections.deque([S])
indegree = [0, 0, 1, 1, 2, 1, 2, 1]  # 진입차수 테이블

while qu:
    node = qu.popleft()
    print(node, end=' ')

    for e in graph[node]:
        indegree[e] -= 1
        if indegree[e] == 0:
            qu.append(e)

# 1 2 5 3 6 4 7
