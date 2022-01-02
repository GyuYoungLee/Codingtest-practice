# [최종 순위] 올해순위 (위상정렬)

# 인접리스트를 이용하면 시간초과 => 인접행렬

import collections
import sys

tc = int(input())
result = []

for _ in range(tc):
    n = int(input())
    rank = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(input())
    change = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

    graph = [[0] * (n + 1) for _ in range(n + 1)]  # 인접 행렬
    indegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            a = rank[i]
            b = rank[j]
            graph[a][b] = 1
            indegree[b] += 1

    for a, b in change:
        if graph[b][a]:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[b] += 1
            indegree[a] -= 1
        else:
            graph[b][a] = 1
            graph[a][b] = 0
            indegree[a] += 1
            indegree[b] -= 1

    qu = collections.deque([i for i, x in enumerate(indegree) if x == 0 and i != 0])

    new_rank = []
    cycle = True if len(qu) == 0 else False
    toomany = False

    while qu:
        now = qu.popleft()
        new_rank.append(now)

        for e in range(1, n + 1):
            if graph[now][e]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    qu.append(e)

        if len(qu) == 0 and len(new_rank) < n:  # 사이클이 발생하는 경우
            cycle = True
            break

        elif len(qu) >= 2:  # 여러 경로가 존재하는 경우
            toomany = True
            break

    if cycle:
        result.append('IMPOSSIBLE')
    elif toomany:
        result.append('?')
    else:
        result.append(' '.join(map(str, new_rank)))

for x in result:
    print(x)
