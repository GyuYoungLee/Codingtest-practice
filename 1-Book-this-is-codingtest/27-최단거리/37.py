# [플로이드] 모든 도시 사이의 이동비용 (플로이드워셜)

import sys

n = int(input())
m = int(input())

INF = int(1e9)
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().rstrip().split())
    if w < dist[a][b]:  # 노선 중 최소비용으로 저장
        dist[a][b] = w

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 갈수 없는 경우에 0으로 출력
        print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
    print()
