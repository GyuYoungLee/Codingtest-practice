# [못생긴 수] n번째 못생긴 수 (DP)

target = 10
dp = [{2, 3, 5}]

while True:
    temp = set(dp[-1])
    for x in dp[-1]:
        temp.add(x * 2)
        temp.add(x * 3)
        temp.add(x * 5)

    if len(temp) >= target:
        break
    dp.append(temp)

temp |= {1, }
result = sorted(list(temp))[target - 1]
print(result)
