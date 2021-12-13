# [숨바꼭질] 1번 헛간에서의 최단거리 (다익스트라)

import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

qu = []
heapq.heappush(qu, (0, 1))
dist = [int(1e9)] * (n + 1)
dist[1] = 0

while qu:
    d, node = heapq.heappop(qu)
    if d > dist[node]:
        continue

    for e, w in graph[node]:
        nd = d + w
        if nd < dist[e]:
            dist[e] = nd
            heapq.heappush(qu, (nd, e))

max_v = max(dist[1:])
target = [i for i, x in enumerate(dist) if x == max_v]
print(target[0], max_v, len(target))  # 가장 멋 헛간의 번호, 가장 멋 헛간의 거리, 가장 먼 헛간의 개수
