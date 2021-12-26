# [특정 거리의 도시 찾기] 최단 거리가 k인 도시의 번호 (BFS or 다익스트라)

# 탐색 방향: 그래프
# 탐색 조건: dist == -1 (1차원 맵으로 생각하기)
# 탐색 결과: dist += 1

import collections
import sys
input = sys.stdin.readline

n, m, k, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

qu = collections.deque([s])
dist = [-1] * (n + 1)
dist[s] = 0

while qu:
    node = qu.popleft()
    if dist[node] == k:
        break

    for e in graph[node]:
        if dist[e] == -1:
            dist[e] = dist[node] + 1
            qu.append(e)


is_exist = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        is_exist = True

if not is_exist:
    print(-1)
