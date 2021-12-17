# [경쟁적 전염] S초 후에 특정 위치의 바이러스의 종류 (BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] = 0
# 탐색 결과: MAP[x][y] = (바이러스 번호), sec += 1

import collections

n, k = map(int, input().split())

_map = []
virus = []

for i in range(n):
    data = list(map(int, input().split()))
    _map.append(data)
    for j in range(n):
        if data[j] != 0:
            virus.append((data[j], 0, i, j))

ts, tx, ty = map(int, input().split())

virus.sort()
qu = collections.deque(virus)

while qu:
    virus, sec, x, y = qu.popleft()
    if sec == ts:
        break

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if _map[nx][ny] == 0:
                _map[nx][ny] = virus
                qu.append((virus, sec + 1, nx, ny))

print(_map[tx - 1][ty - 1])
