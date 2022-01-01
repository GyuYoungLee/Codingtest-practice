# [크루스칼]

N = 4
parent = [0, 1, 2, 3, 4]  # 부모 테이블


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


edges = [
    (1, 2, 4),
    (2, 2, 3),
    (3, 1, 3),
    (6, 1, 2),
    (9, 3, 4)
]
edges.sort()

total = 0
for cost, v1, v2 in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        total += cost

print(total)  # 6
