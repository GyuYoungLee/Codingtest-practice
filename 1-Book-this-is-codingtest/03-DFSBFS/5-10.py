# [음료수 얼려 먹기] 만들수 있는 아이스크림의 개수 (DFS)

# 탐색방햘: 상하좌우
# 탐색조건: MAP[x][y] == 0
# 탐색결과: MAP[x][y] = 2

def dfs(x, y):
    MAP[x][y] = 2
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 0:
                dfs(nx, ny)


N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)  # 2
