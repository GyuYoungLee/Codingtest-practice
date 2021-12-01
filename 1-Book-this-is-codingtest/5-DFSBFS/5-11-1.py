# [미로 탈출] 목적지까지 도달하는 최소이동횟수 (BFS)

# 탐색방햘: 상하좌우
# 탐색조건: MAP[x][y] = 1
# 탐색결과: MAP[x][y] = 2, count += 1 ==> MAP 방문여부, count 방문회수 저장

import collections

N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]

qu = collections.deque([(0, 0, 1)])

result = 0
while qu:
    x, y, count = qu.popleft()
    if (x, y) == (N - 1, M - 1):
        result = count

    for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 1:
                MAP[nx][ny] = MAP[x][y] + 1
                qu.append((nx, ny, count + 1))

print(result)  # 5
