# 플로이드 워셜 (모든점 -> 모든점 최단거리)

N = 4
INF = int(1e9)

# 최단거리 테이블
dist = [
  [0,     4,  INF,    6],
  [3,     0,    7,  INF],
  [5,   INF,    0,    4],
  [INF, INF,    2,    0]
]

# n1 -> n2 경로에 대해 n1 -> k -> n2 로 업데이트한다 (DP)
for k in range(N):
    for n1 in range(N):
        for n2 in range(N):
            dist[n1][n2] = min(dist[n1][n2], dist[n1][k] + dist[k][n2])

for i in range(N):
    print(dist[i])

# [0,  4,  8,  6]
# [3,  0,  7,  9]
# [5,  9,  0,  4]
# [7, 11,  2,  0]
