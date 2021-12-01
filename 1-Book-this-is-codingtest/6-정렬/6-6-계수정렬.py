# [계수 정렬]

a = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt_list = [0] * (max(a) + 1)
for x in a:
    cnt_list[x] += 1

for i, cnt in enumerate(cnt_list):
    for _ in range(cnt):
        print(i, end=' ')

# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
