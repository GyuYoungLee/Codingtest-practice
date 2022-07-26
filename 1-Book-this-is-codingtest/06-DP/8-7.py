# [바닥 공사] 모든 경우의 수 (DP)

# dp[i] = (길이 i일때) 바닥을 채우는 경우의 수
#       = dp[i-1] + dp[i-2] * 2

N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 796796

print(dp[N])  # 5
