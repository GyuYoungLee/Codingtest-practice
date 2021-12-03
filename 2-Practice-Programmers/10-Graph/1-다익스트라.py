# [가장 먼 노드] 1번 노드에서 가장 먼 노드의 개수 (다익스트라)

import heapq


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append([b, 1])
        graph[b].append([a, 1])

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

    result = len([x for x in dist[1:] if x == max(dist[1:])])
    return result


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
