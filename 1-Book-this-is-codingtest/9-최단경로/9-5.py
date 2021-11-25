# 전보: 모든 도시에 도달하는 최종 시간 (다익스트라)

import heapq

N, M, C = map(int, input().split())

graph = [[] for i in range(N + 1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    graph[n1].append([n2, w])

INF = int(1e9)
dist = [INF] * (N + 1)  # 최단거리 테이블

dist[C] = 0
qu = []
heapq.heappush(qu, (0, C))

while qu:
    d, node = heapq.heappop(qu)
    if d > dist[node]:
        continue

    for e, w in graph[node]:
        nd = d + w
        if nd < dist[e]:
            dist[e] = nd
            heapq.heappush(qu, [nd, e])

count = len([x for x in dist if x != INF]) - 1
hour = max([x for x in dist if x != INF])
print(count, hour)
