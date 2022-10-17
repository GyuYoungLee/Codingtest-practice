# [계수 정렬]

a = [0, 3, 1, 2, 1, 5, 2]

check = [0] * (max(a) + 1)

for x in a:
    check[x] += 1

result = []
for i, x in enumerate(check):
    result.extend([i] * x)

print(result)  # [0, 1, 1, 2, 2, 3, 5]
