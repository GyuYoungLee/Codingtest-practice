# [게임개발] 상하좌우 이동이 가능할 때 탐색 (구현)

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

_map[x][y] = 2
count = 1
turn_times = 0

while True:
    direction = 3 if direction == 0 else direction - 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 앞으로 이동
    if _map[nx][ny] == 0:  # 탐색 조건 (육지)
        x = nx
        y = ny
        _map[nx][ny] = 2  # 탐색 결과
        count += 1
        turn_times = 0

    # 방향 전환
    else:
        turn_times += 1

    # 뒤로 이동
    if turn_times == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if _map[nx][ny] == 1:  # 종료 조건 (바다)
            break
        else:
            x = nx
            y = ny
            turn_times = 0


print(count)  # 3
