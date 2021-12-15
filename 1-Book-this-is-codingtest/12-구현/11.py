# [뱀] 뱀이 이동하는 최종시간 (구현, 시뮬레이션)

n = int(input())
k = int(input())

_map = [[0] * (n + 1) for _ in range(n + 1)]
event = {}

for _ in range(k):
    x, y = map(int, input().split())
    _map[x][y] = 1  # 사과

e = int(input())
for _ in range(e):
    s, d = input().split()
    event[int(s)] = d


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
x, y, direction = 1, 1, 0
_map[x][y] = 2  # 뱀
snake = [(x, y)]

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx <= n and 1 <= ny <= n and _map[nx][ny] != 2:
        if _map[nx][ny] == 0:
            _map[nx][ny] = 2  # 머리 추가
            snake.append((nx, ny))
            px, py = snake.pop(0)
            _map[px][py] = 0  # 꼬리 제외
        # 사과
        elif _map[nx][ny] == 1:
            _map[nx][ny] = 2
            snake.append((nx, ny))
    else:
        break

    # 반복 설정
    x, y = nx, ny
    if event.get(time):
        if event[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)
