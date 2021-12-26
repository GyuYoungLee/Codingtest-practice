# [계수 정렬]

a = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

check = [0] * (max(a) + 1)
for x in a:
    check[x] += 1

for i in range(10):
    for _ in range(check[i]):
        print(i, end=' ')

# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
