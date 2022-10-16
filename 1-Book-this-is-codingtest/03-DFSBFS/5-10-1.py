# [음료수 얼려 먹기] 만들수 있는 아이스크림의 개수 (DFS)

# 탐색 방햘: 상하좌우
# 탐색 조건: map[x][y] == 0
# 탐색 결과: map[x][y] = 2

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]


# MAP 경계를 이동불가 영역으로 만들어서 경계검사를 생략하는 방법
_map = [[1] * (m + 2) for _ in range(n + 2)]
for i in range(n):
    for j in range(m):
        _map[i + 1][j + 1] = data[i][j]


def dfs(x, y):
    _map[x][y] = 2

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if _map[nx][ny] == 0:
            dfs(nx, ny)


count = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if _map[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)  # 2
