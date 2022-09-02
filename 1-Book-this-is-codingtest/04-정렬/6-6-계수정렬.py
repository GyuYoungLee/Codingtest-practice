# [계수 정렬]

a = [7, 5, 8, 0, 3, 1, 6, 2, 8, 1, 4, 8, 0, 5, 2]

check = [0] * (max(a) + 1)
for x in a:
    check[x] += 1

result = []
for i, x in enumerate(check):
    for _ in range(x):
        result.append(i)

print(result)
# [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8]
