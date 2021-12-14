# [어두운 길] 제오된 경로로 절약할 수 있는 금액 (크루스칼)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

total = 0
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))
    total += w

edges.sort()

parent = list(range(n + 1))

mst = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        mst += w

print(total - mst)  # 제외된 경로로 절약할 수 있는 금액
