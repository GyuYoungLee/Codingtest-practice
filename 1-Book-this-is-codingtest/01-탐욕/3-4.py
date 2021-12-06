# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

n, k = map(int, input().split())

# 풀이 1
count = 0
while n >= k:
    while n % k != 0:
        n -= 1
        count += 1

    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)  # 3
