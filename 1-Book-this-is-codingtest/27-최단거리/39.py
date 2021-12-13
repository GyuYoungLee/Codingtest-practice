# [화성 탐사] 왼쪽 위에서 오른쪽 아래로 가는 최단거리 (다익스트라)

import heapq

result = []
tc = int(input())

for _ in range(tc):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    qu = []
    heapq.heappush(qu, (a[0][0], 0, 0))
    dist = [[int(1e9)] * n for _ in range(n)]
    dist[0][0] = a[0][0]

    while qu:
        d, x, y = heapq.heappop(qu)
        if d > dist[x][y]:
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + a[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(qu, (nd, nx, ny))

    result.append(dist[n - 1][n - 1])

for x in result:
    print(x)
