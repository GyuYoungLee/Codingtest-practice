# 도시 분할 계획: 모든 집을 연결하는 경로의 최소유지비 (크루스칼)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = list(range(v + 1))

edges = []
for _ in range(e):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))

edges.sort()

total_cost = last_cost = 0
for cost, v1, v2 in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        total_cost += cost
        last_cost = cost  # 최소신장트리에 포함되는 간선 중에서 가장 비용이 큰 간선

print(total_cost - last_cost)  # 8
