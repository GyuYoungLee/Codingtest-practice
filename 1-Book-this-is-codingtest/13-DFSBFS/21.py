# [인구 이동] 인구이동이 몇번 발생하는지 (완전탐색 + BFS/DFS)

# 참조: 5-10 문제와 동일

# 탐색 방향: 상하좌우
# 탐색 조건: visited[x][y] == 0, low <= 인구차 <= high
# 탐색 결과: visited[x][y] = 1,  인구 배분

import collections

n, low, high = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]


def move(si, sj):
    qu = collections.deque([(si, sj)])
    visited[si][sj] = 1

    count = 0
    total = 0
    country = []

    # 대상국가 탐색
    while qu:
        x, y = qu.popleft()
        count += 1
        total += _map[x][y]
        country.append((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and low <= abs(_map[x][y] - _map[nx][ny]) <= high:
                    visited[nx][ny] = 1
                    qu.append((nx, ny))

    # 대상국가들 간 인구이동
    for i, j in country:
        _map[i][j] = total // count


# 더이상 인구 이동이 발생하지 않을 때까지 반복
turn = 0
while True:
    visited = [[0] * n for _ in range(n)]

    # 모든 위치마다 반복
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count += 1
                move(i, j)

    # 더이상 인구이동이 발생하지 않는 경우
    if count == n * n:
        break

    turn += 1

print(turn)
