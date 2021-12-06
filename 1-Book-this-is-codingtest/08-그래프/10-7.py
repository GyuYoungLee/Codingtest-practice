# [팀 결성] 같은 팀 여부 확인 (서로소 집합)

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


N, M = map(int, input().split())
parent = list(range(N + 1))

for _ in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

# NO NO YES
