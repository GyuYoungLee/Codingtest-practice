# [음료수 얼려 먹기] 만들수 있는 아이스크림의 개수 (DFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] = 0
# 탐색 결과: MAP[x][y] = 2

def dfs(x, y):
    MAP[x][y] = 2
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if MAP[nx][ny] == 0:
            dfs(nx, ny)


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

# MAP 경계를 이동불가 영역으로 만들어서 경계검사를 생략하는 방법
MAP = [[1] * (M + 2) for _ in range(N + 2)]
for x in range(N):
    for y in range(M):
        MAP[x + 1][y + 1] = data[x][y]

count = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if MAP[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)  # 2
