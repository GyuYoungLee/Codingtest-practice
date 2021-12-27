# [화폐구성 = 거스름돈] 금액을 만드는 화폐의 최소 갯수 (DP)

#  dp[i] = i를 만드는 화폐의 최소 갯수
#        = min(dp[i-k]) + 1

N, M = map(int, input().split())
coin_types = [int(input()) for _ in range(N)]

dp = [10001] * (M + 1)  # 최소값을 구하므로 큰값으로 초기화
dp[0] = 0

for i in range(1, M + 1):
    for coin in coin_types:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[M] if dp[M] != 10001 else -1)  # 5
