# [왕실의 나이트] 다음 위치가 여러개가 가능할 때 (구현)

steps = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
         (1, 2), (2, 1), (2, -1), (1, -2)]

position = input()
x = int(position[1])
y = ord(position[0]) - ord('a') + 1

count = 0
for dx, dy in steps:  # 다음 위치에 8개 가능
    nx = x + dx
    ny = y + dy

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)  # 2
