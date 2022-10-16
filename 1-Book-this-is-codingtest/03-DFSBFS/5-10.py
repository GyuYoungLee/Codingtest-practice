# [음료수 얼려 먹기] 만들수 있는 아이스크림의 개수 (DFS)

# 탐색 방햘: 상하좌우
# 탐색 조건: map[x][y] == 0
# 탐색 결과: map[x][y] = 2

n, m = map(int, input().split())
_map = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    _map[x][y] = 2

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if _map[nx][ny] == 0:
                dfs(nx, ny)


count = 0

for i in range(n):
    for j in range(m):
        if _map[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)  # 2
