# [연구소] 바이러스 전파 후 안전영역의 최대값 (재귀 + DFS/BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] == 0
# 탐색 결과: MAP[x][y] = 2

n, m = map(int, input().split())

_map = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    _map.append(data)


def virus(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def make(wall):
    global result

    # 벽 3개 설치
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = _map[i][j]

        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전영역 계산
        count = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    count += 1

        result = max(result, count)
        return

    for i in range(n):
        for j in range(m):
            if _map[i][j] == 0:
                _map[i][j] = 1
                make(wall + 1)
                _map[i][j] = 0


result = 0
make(0)
print(result)
