# [네트워크] 네트워크의 개수 (dfs)

def solution(n, computers):
    # dfs
    def dfs(x):
        visited[x] = 1
        for e in graph[x]:
            if not visited[e]:
                dfs(e)

    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i + 1].append(j + 1)

    visited = [0] * (n + 1)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            count += 1
            dfs(i)

    return count


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
