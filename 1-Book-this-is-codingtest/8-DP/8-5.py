# [1 만들기] 연산횟수의 최소값 (DP)

# dp[i] = i를 1로 만드는 연산 횟수의 최소값
#       = min(dp[i-1], dp[i/2], dp[i/3], dp[i/5]) + 1

X = int(input())

dp = [X] * (X + 1)  # 최소값을 구하므로 큰값으로 초기화
dp[1] = 0

for i in range(3, X + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[X])  # 3
