# [상하좌우] 순차적으로 다음 위치로 이동 (구현)

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
plans = input().split()

x = 1
y = 1

for plan in plans:
    i = move_types.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= n and 1 <= ny <= n:
        x = nx
        y = ny

print(x, y)  # 3 4
