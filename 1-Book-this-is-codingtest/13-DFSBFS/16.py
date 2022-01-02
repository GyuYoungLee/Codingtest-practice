# [연구소] 바이러스 전파 후 안전영역의 최대값 (조합 + DFS/BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] == 0
# 탐색 결과: MAP[x][y] = 2

import collections
import copy
import itertools

n, m = map(int, input().split())

_map = []
space = []
virus = []

for i in range(n):
    data = list(map(int, input().split()))
    _map.append(data)
    for j in range(m):
        if data[j] == 0:
            space.append((i, j))
        elif data[j] == 2:
            virus.append((i, j))

result = 0
for candidates in itertools.combinations(space, 3):
    temp = copy.deepcopy(_map)

    # 벽 3개 설치
    for i, j in candidates:
        temp[i][j] = 1

    # 바이러스 전파
    qu = collections.deque(virus)
    while qu:
        x, y = qu.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    qu.append((nx, ny))

    # 안전영역 계산
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    result = max(result, count)

print(result)
