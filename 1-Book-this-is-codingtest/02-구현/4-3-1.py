# [왕실의 나이트] 이동 가능한 모든 경우의 수 (구현)

position = input()
x = int(position[1])
y = ord(position[0]) - ord('a') + 1

steps = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
         (1, 2), (2, 1), (2, -1), (1, -2)]

count = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)  # 2
