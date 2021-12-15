# [네트워크] 네트워크의 개수 (dfs)

def solution(n, computers):
    # dfs
    def dfs(x):
        visited[x] = 1
        for j in range(1, n + 1):
            if computers[x - 1][j - 1] == 1:
                if not visited[j]:
                    dfs(j)

    visited = [0] * (n + 1)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            dfs(i)

    return count


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
