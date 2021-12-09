# [여행경로] 방문경로 (dfs)

# 탐색방향: 간선
# 탐색조건: 간선 in routes
# 탐색결과: routes.remove(간선)

import collections


def solution(tickets):
    result = []

    def dfs(s, footprint):
        if not routes:
            result.append(footprint[:])
            return

        for e in graph[s]:
            if (s, e) in routes:
                routes.remove((s, e))
                dfs(e, footprint + [e])
                routes.append((s, e))

    # graph: {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']})
    # routes: [('ICN', 'JFK'), ('HND', 'IAD'), ('JFK', 'HND')]
    graph = collections.defaultdict(list)
    routes = []

    for s, e in tickets:
        graph[s].append(e)
        routes.append((s, e))

    for k in graph:
        graph[k].sort()

    dfs('ICN', ["ICN"])
    return result[0]  # 알파벳 순서가 앞서는 경로


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["ICN", "COO"], ["BOO", "ICN"], ["COO", "BOO"], ["COO", "ICN"]]))
# ["ICN", "BOO", "ICN", "COO", "ICN", "COO", "BOO"]
