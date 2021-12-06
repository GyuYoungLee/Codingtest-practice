# [왕실의 나이트] 이동 가능한 모든 경우의 수 (구현)

position = input()
x = int(position[1])
y = ord(position[0]) - ord('a') + 1

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)  # 2
