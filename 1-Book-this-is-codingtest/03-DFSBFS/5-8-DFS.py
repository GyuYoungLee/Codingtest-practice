# [DFS]

n = 4
graph = [
    [],
    [2, 3],
    [1, 3, 4],
    [1, 2, 4],
    [2, 3]
]

s = 1
visited = [0] * (n + 1)  # 방문 테이블


def dfs(v):
    visited[v] = 1
    print(v)

    for e in graph[v]:
        if not visited[e]:
            dfs(e)


dfs(s)
