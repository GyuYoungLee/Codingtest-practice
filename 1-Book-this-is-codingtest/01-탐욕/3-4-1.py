# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

n, k = map(int, input().split())

count = 0

# 풀이 2 (개선)
while n != 1:

    if n % k == 0:
        n //= k
        count += 1

    elif n > k:
        target = n // k * k
        count += n - target
        n = target

    else:
        count = n - 1
        n = 1

print(count)
