# [정수 삼각형] 거쳐간 숫자의 최대값 (dp)

def solution(tri):
    n = len(tri)
    dp = [[-1] * (i + 1) for i in range(n)]
    dp[0][0] = tri[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            # 위 왼쪽: dp[i - 1][j - 1]
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + tri[i][j])

            # 위 오른쪽: dp[i - 1][j]
            if j <= i - 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + tri[i][j])

    return max(dp[n - 1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))  # 30
