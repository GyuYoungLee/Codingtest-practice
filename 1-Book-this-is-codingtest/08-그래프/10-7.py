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


n, m = map(int, input().split())
parent = list(range(n + 1))
data = [list(map(int, input().split())) for _ in range(m)]

for op, a, b in data:
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

# NO NO YES
