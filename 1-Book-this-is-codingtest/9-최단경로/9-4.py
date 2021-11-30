# 미래도시: 1 -> K -> X 로 이동하는 최소 시간  (플로이드워셜)

N, M = map(int, input().split())

INF = int(1e9)
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dist[i][i] = 0

for _ in range(M):
    n1, n2 = map(int, input().split())
    dist[n1][n2] = 1
    dist[n2][n1] = 1

X, K = map(int, input().split())

for k in range(1, N + 1):
    for n1 in range(1, N + 1):
        for n2 in range(1, N + 1):
            dist[n1][n2] = min(dist[n1][n2], dist[n1][k] + dist[k][n2])

# 1 -> K -> X 이동시 최단 거리
result = dist[1][K] + dist[K][X]
print(result if result < INF else -1)  # 3
