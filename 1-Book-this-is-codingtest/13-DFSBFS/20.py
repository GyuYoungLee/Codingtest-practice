# [감시 피하기] 선생님이 학생을 탐색할수 있는지 (조합 + DFS/BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] == 'X'
# 탐색 결과:

import collections
import copy
import itertools

n = int(input())

_map = []
space = []
teacher = []

for i in range(n):
    _map.append(list(input().split()))
    for j in range(n):
        if _map[i][j] == 'X':
            space.append((i, j))
        elif _map[i][j] == 'T':
            teacher.append((i, j, 1, 0))
            teacher.append((i, j, -1, 0))
            teacher.append((i, j, 0, 1))
            teacher.append((i, j, 0, -1))


result = 'NO'
for candidates in itertools.combinations(space, 3):
    temp = copy.deepcopy(_map)

    # 장애물 3개 추가
    for i, j in candidates:
        temp[i][j] = 'O'

    # 선생님 감시 활성화
    watch = False
    qu = collections.deque(teacher)

    while qu:
        x, y, dx, dy = qu.popleft()

        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if temp[nx][ny] == 'S':
                watch = True
                break
            elif temp[nx][ny] == 'X':
                qu.append((nx, ny, dx, dy))

    # 결과처리
    if not watch:
        result = 'YES'
        break

print(result)
