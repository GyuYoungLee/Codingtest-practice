# [볼링공 고르기] 볼링공을 고르는 경우의 수 (탐욕)

import collections

n, m = map(int, input().split())
a = list(map(int, input().split()))

count_w = collections.Counter(a)

total = 0
for i in range(1, m + 1):  # 무게 1 ~ m 까지 고려
    n -= count_w[i]
    total += count_w[i] * n

print(total)
