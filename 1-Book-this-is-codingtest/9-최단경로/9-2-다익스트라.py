# [다익스트라] 출발점 -> 모든점 최단거리

import heapq

N = 4
graph = [
    [],
    [(2, 6), (3, 3)],
    [(1, 6), (3, 2), (4, 1)],
    [(1, 3), (2, 2), (4, 9)],
    [(2, 1), (3, 9)]
]
S = 1

qu = []
heapq.heappush(qu, (0, S))
dist = [int(1e9)] * (N + 1)  # 최단거리 테이블
dist[S] = 0

while qu:
    d, node = heapq.heappop(qu)
    if d > dist[node]:
        continue

    for e, w in graph[node]:
        nd = d + w
        if nd < dist[e]:
            dist[e] = nd
            heapq.heappush(qu, (nd, e))

print(dist)  # [1000000000, 0, 5, 3, 6]
