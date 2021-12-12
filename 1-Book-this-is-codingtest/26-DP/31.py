# [금광] 열 방행으로 이동시 채취된 금의 최대량 (DP)

# dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + a[i][j]

tc = int(input())

result = []
for _ in range(tc):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    _map = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            _map[i][j] = data[m * i + j]

    dp = [[0] * (m + 1) for _ in range(n + 2)]

    max_v = 0
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + _map[i - 1][j - 1]
            max_v = max(max_v, dp[i][j])

    result.append(max_v)

for x in result:
    print(x)
