# [DFS]

N = 4
graph = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3]
]

S = 1
visited = [0] * (N + 1)  # 방문 테이블


def dfs(v):
    visited[v] = 1
    print(v, end=' ')  # 탐색

    for e in graph[v]:
        if not visited[e]:
            dfs(e)


dfs(S)
