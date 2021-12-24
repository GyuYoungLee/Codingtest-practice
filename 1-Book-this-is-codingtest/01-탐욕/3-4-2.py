# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

n, k = map(int, input().split())

# 풀이 3 (DP)
dp = [n] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % k == 0:
        dp[i] = dp[i // k] + 1

print(dp[n])
