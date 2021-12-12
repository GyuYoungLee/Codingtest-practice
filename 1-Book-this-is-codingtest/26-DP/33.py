# [퇴사] 상담결과 최대수익 (DP)

# dp[i] = max(해당일 상담을 안하는 경우, 해당일 상담을 하는 경우)
#       = max(dp[i+1]            , dp[i+t[i]] + a[i])

n = int(input())
t = []
a = []
for _ in range(n):
    tt, aa = map(int, input().split())
    t.append(int(tt))
    a.append(int(aa))

dp = [0] * (n + 1)
dp[n] = 0

# 뒤의 값으로부터 앞의 값을 구한다
for i in range(n - 1, -1, -1):
    # 해당일 상담을 안하는 경우
    dp[i] = dp[i + 1]

    # 해당일 상담을 하는 경우
    time = i + t[i]
    if time <= n:
        dp[i] = max(dp[i], dp[time] + a[i])

print(dp[0])
