# [개미 전사] 약탈가능한 식량의 최대값 (DP)

# dp[i] = (식량창고 i개일 때) 약탈하는 식량의 최대값
#       = max(dp[i-1], dp[i-2] + a[i])

N = int(input())
a = list(map(int, input().split()))

dp = [0] * N
dp[0] = a[0]
dp[1] = max(a[0], a[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + a[i])

print(dp[N - 1])  # 8
