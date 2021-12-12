# [못생긴 수] n번째 못생긴 수 (DP)

target = 10

dp = [1]
i = j = k = 0
m2, m3, m5 = 2, 3, 5
#            4, 6, 10
#            6, 9, 15

while True:
    min_v = min(m2, m3, m5)
    dp.append(min_v)

    if len(dp) == target:
        break

    if min_v == m2:
        i += 1
        m2 = dp[i] * 2

    if min_v == m3:
        j += 1
        m3 = dp[j] * 3

    if min_v == m5:
        k += 1
        m5 = dp[k] * 5

print(dp)
print(dp[-1])
