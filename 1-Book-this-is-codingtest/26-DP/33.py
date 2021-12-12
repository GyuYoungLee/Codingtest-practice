# [퇴사] 상담결과로 얻을수 있는 최대 수익 (DP)

# dp[i] = max(해당일 상담을 안하는 경우, 해당일 상담을 하는 경우)
#       = max(dp[i+1]            , a[i] + dp[time])

n = int(input())
t = []
a = []
for _ in range(n):
    tt, aa = map(int, input().split())
    t.append(int(tt))
    a.append(int(aa))

dp = [0] * (n + 1)

# 뒤의 값으로부터 앞의 값을 구한다
for i in range(n - 1, -1, -1):

    # 해당일 상담을 안하는 경우
    dp[i] = dp[i + 1]

    # 해당일 상담을 하는 경우
    time = i + t[i]
    if time <= n:
        dp[i] = max(dp[i], a[i] + dp[time])

print(dp[0])
