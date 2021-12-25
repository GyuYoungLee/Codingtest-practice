# [감시 피하기] 선생님이 학생을 탐색할수 있는지 (재귀 + DFS/BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] != 'O'
# 탐색 결과: MAP[x][y] = 'T'

import copy
import collections

n = int(input())

_map = []
teacher = []

for i in range(n):
    _map.append(list(input().split()))
    for j in range(n):
        if _map[i][j] == 'T':
            teacher.append((i, j, 1, 0))
            teacher.append((i, j, -1, 0))
            teacher.append((i, j, 0, 1))
            teacher.append((i, j, 0, -1))

result = "NO"


def dfs(obstacle):
    global result

    # 장애물 3개 추가
    if obstacle == 3:
        temp = copy.deepcopy(_map)

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
                elif temp[nx][ny] != 'O':
                    temp[nx][ny] = 'T'
                    qu.append((nx, ny, dx, dy))

        if not watch:
            result = "YES"

        return

    for i in range(n):
        for j in range(n):
            if _map[i][j] == 'X':
                _map[i][j] = 'O'
                dfs(obstacle + 1)
                _map[i][j] = 'X'


dfs(0)
print(result)