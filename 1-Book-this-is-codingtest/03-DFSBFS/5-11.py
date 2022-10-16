# [미로 탈출] 목적지까지 도달하는 최소이동횟수 (BFS)

# 탐색 방햘: 상하좌우
# 탐색 조건: map[x][y] == 1
# 탐색 결과: map[x][y] = map[x'][y'] + 1 ==> map 에 방문여부, 방문회수 저장

import collections

n, m = map(int, input().split())
_map = [list(map(int, input())) for _ in range(n)]

qu = collections.deque([(0, 0)])
_map[0][0] = 1

while qu:
    x, y = qu.popleft()

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if _map[nx][ny] == 1:
                qu.append((nx, ny))
                _map[nx][ny] = _map[x][y] + 1

print(_map[n - 1][m - 1])
