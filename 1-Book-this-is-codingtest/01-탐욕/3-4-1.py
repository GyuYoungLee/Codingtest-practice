# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

n, k = map(int, input().split())

# 풀이 2 (개선)
count = 0
while n >= k:
    if n % k != 0:
        target = n // k * k
        count += n - target
        n = target

    n //= k
    count += 1

count += n - 1

print(count)  # 3
