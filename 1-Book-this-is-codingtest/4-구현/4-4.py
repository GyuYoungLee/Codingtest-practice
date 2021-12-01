# [게임개발] 캐릭터가 방문한 칸의 수 (구현)

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

MAP = []
for _ in range(n):
    MAP.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]
visited[x][y] = 1

count = 1
turn_times = 0
while True:
    direction = direction - 1 if direction != 0 else 3
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 앞으로 이동
    if MAP[nx][ny] == 0 and not visited[nx][ny]:
        x = nx
        y = ny
        visited[x][y] = 1
        count += 1
        turn_times = 0

    # 방향 전환
    else:
        turn_times += 1

    # 뒤로 이동
    if turn_times == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if MAP[nx][ny] == 0:
            x = nx
            y = ny
            turn_times = 0
        else:
            break

print(count)  # 3
