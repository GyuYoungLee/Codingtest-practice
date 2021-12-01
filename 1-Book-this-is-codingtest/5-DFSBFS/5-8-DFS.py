# DFS

N = 4
graph = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3]
]
S = 1


def dfs(node):
    visited[node] = 1
    print(node, end=' ')  # 탐색
    for e in graph[node]:
        if not visited[e]:
            dfs(e)


visited = [0] * (N + 1)
dfs(S)
