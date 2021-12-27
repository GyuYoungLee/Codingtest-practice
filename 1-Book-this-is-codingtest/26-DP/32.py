# [정수 삼각형] 행 방향으로 이동시 숫자합의 최대값 (DP)

# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]

n = int(input())
_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(n)]
dp[0][0] = _map[0][0]

# 행 방향으로 이동
for i in range(1, n):
    for j in range(i + 1):
        if j != 0:
            dp[i][j] = dp[i - 1][j - 1] + _map[i][j]
        if j != i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + _map[i][j])

print(max(dp[n - 1]))
