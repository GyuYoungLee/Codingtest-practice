# [1이 될때까지] 최소 연산횟수 (탐욕 or DP)

N, K = map(int, input().split())

# 풀이 3 (DP)
dp = [N] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % K == 0:
        dp[i] = min(dp[i], dp[i // K] + 1)

print(dp[N])
