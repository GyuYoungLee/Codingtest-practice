# [게임개발] 상하좌우 이동이 가능할 때 탐색 (구현)

n, m = map(int, input().split())
x, y, d = map(int, input().split())

_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

_map[x][y] = 2
count = 1
turn = 0

while True:
    d = d - 1 if d != 0 else 3
    nx = x + dx[d]
    ny = y + dy[d]

    # 앞으로 이동
    if _map[nx][ny] == 0:
        count += 1
        _map[nx][ny] = 2

        x = nx
        y = ny
        turn = 0

    # 뒤로 이동
    elif turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if _map[nx][ny] == 1:
            break

        x = nx
        y = ny
        turn = 0

    # 방향 전환
    else:
        turn += 1

print(count)  # 3
