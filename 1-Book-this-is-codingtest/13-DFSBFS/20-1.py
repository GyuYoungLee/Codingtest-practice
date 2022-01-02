# [감시 피하기] 선생님이 학생을 탐색할수 있는지 (재귀 + DFS/BFS)

# 탐색 방향: 상하좌우
# 탐색 조건: MAP[x][y] == 'X'
# 탐색 결과:

n = int(input())

_map = []
temp = [[0] * n for _ in range(n)]
teacher = []

for i in range(n):
    _map.append(list(input().split()))
    for j in range(n):
        if _map[i][j] == 'T':
            teacher.append((i, j, 1, 0))
            teacher.append((i, j, -1, 0))
            teacher.append((i, j, 0, 1))
            teacher.append((i, j, 0, -1))


def is_watch(x, y, dx, dy):
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < n:
        if temp[nx][ny] == 'S':
            return True
        elif temp[nx][ny] == 'X':
            return is_watch(nx, ny, dx, dy)
    return False


def make(obstacle):
    global result

    if obstacle == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = _map[i][j]

        watch = False
        for x, y, dx, dy in teacher:
            if is_watch(x, y, dx, dy):
                watch = True
                break

        if not watch:
            result = 'YES'
        return

    for i in range(n):
        for j in range(n):
            if _map[i][j] == 'X':
                _map[i][j] = 'O'
                make(obstacle + 1)
                _map[i][j] = 'X'


result = "NO"
make(0)
print(result)
