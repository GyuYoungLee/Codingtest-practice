# [도둑질] 훔칠수 있는 돈의 최대값 (dp)

# dp[i] = max(dp[i-2] + a[i], dp[i-1])
# 첫번째 집과 마지막 집이 이웃이라는 점을 고려해야 한다

def solution(money):
    n = len(money)

    # 첫번째 집을 훔치는 경우 (마지막 집을 훔칠수 없다)
    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n - 1):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])

    # 첫번째 집을 훔치지 않는 경우 (마지막 집을 훔칠수 있다)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])

    return max(max(dp), max(dp2))


print(solution([1, 2, 3, 1]))  # 4
