# [왕실의 나이트] 다음 위치가 여러개가 가능할 때 (구현)

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

position = input()

x = int(position[1])
y = ord(position[0]) - ord('a') + 1

count = 0

for i in range(8):  # 다음 위치에 8개 가능
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)  # 2
