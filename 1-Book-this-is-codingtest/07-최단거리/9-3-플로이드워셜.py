# [플로이드워셜] 모든점 -> 모든점 최단거리

N = 4

# 거리 테이블
INF = int(1e9)
dist = [
  [0,     6,    3,  INF],
  [6,     0,    2,    1],
  [3,     2,    0,    9],
  [INF,   1,    9,    0]
]

# n1 -> n2 경로에 대해 n1 -> k -> n2 로 업데이트한다 (DP)
for k in range(N):
    for n1 in range(N):
        for n2 in range(N):
            dist[n1][n2] = min(dist[n1][n2], dist[n1][k] + dist[k][n2])

for i in range(N):
    print(dist[i])

# [0,  5,  3,  6]
# [5,  0,  2,  1]
# [3,  2,  0,  3]
# [6,  1,  3,  0]
